from mafiagg.roles import GetRole
from mafiagg.decks import GetDeck
from mafiagg.user import GetUser
from mafiagg.room import GetRoom
from mafiagg.setups import GetSetup
from mafiagg.settings import EditSetting
from mafiagg.helper.decorators import (
    ignore_bot_message,
    register_command,
)
from mafiagg.helper.tools import (
    convert_setup,
    get_role_count,
)
from mafiagg.credential_manager import CredentialManager
from mafiagg.bot.botbase import BotBase
from typing import Dict, List, Union


class UserCache:
    data = dict()


class Bot(BotBase):
    def __init__(
        self,
        auth: CredentialManager,
        command_prefix: str = "$",
        admin_users: List[int] = [],
    ):
        self.command_prefix = command_prefix
        self.admin_users = admin_users
        self.cred = auth
        self.botUser = auth.get_user()
        self.cookie = auth.get_cookie_data()
        self.response = {"type": "chat", "message": "Couldn't parse command"}
        self.rname, self.isUnlisted = None, None
        self.cache = UserCache()
        self.roleCache = {}  # TODO: Improve
        self.register_bot_commands()
        self.register_modules()

    def register_modules(self):
        self.Role = GetRole()
        self.Deck = GetDeck(cookie=self.cookie)
        self.User = GetUser()
        self.Room = GetRoom(cookie=self.cookie)
        self.Setup = GetSetup()
        self.Setting = EditSetting()

    def stop(self):
        self.cred.logout()

    def reset_cache(self):
        self.cache.data = dict()
    @ignore_bot_message
    def parse(self, payload: Dict) -> Union[Dict, None]:
        if payload["type"] == "chat":
            msg = payload["message"]
            user = payload["from"]["userId"]

            if msg[0] != self.command_prefix:
                return
            cmd, args = self.parseCommand(msg[1:])
            if cmd == None:
                pass
            if cmd.isAdmin and user not in self.admin_users:
                return {
                    "type": "chat",
                    "message": "❌ You do not have permission to run this command",
                }

            # cmd = self.getCommand(cmd)
            if callable(cmd) and cmd.__doc__:
                if args is not None:
                    data = cmd(args)
                else:
                    try:
                        data = cmd()
                    except TypeError:
                        return self.send(
                            f"✅ Command [{cmd._commandName}] : {cmd.__doc__}"
                        )
                return data
            else:
                return
        elif payload["type"] == "userJoin":
            return self._welcome(payload["userId"])
        else:
            return

    @register_command("get deck")
    def deck(self, args) -> Dict:
        """Search for a deck (name)"""
        deckData = self.Deck.get_deck(args)
        self.response["message"] = deckData
        return self.response

    @register_command("use deck", isAdmin=True)
    def usedeck(self, args) -> Union[Dict, List]:
        """Change the current deck (give name)"""
        if args.lower() == "random":
            deckID = self.Deck.get_random_deck()
            match = self.Deck.get_deck_by_id(id=deckID)
            deckName = match.name
        else:
            match = self.Deck.get_deck(args, format=False)
            if not match:
                response = self.send(f"⛔ Could not find a deck with the name {args}")
                return self.response
            deckID = match.key
            deckName = match.name
        response = self.send(f"✅ Set deck to {deckName}")
        return [{"type": "options", "deck": deckID}, response]

    @register_command("get role")
    def role(self, args) -> Dict:
        """Search for a role (name)"""
        roleData, _ = self.Role.get_role(name=args)
        self.response["message"] = roleData
        return self.response

    @register_command("get setup")
    def setup(self, args) -> Dict:
        """Search for a setup (name)"""
        setupData, _ = self.Setup.get_setup(args)
        self.response["message"] = setupData
        return self.response

    @register_command("use setup", isAdmin=True)
    def usesetup(self, args) -> Union[Dict, List]:
        """Change the current setup (give name)"""
        # infer whether setup code or name
        try:
            assert int(args[:2]) and " " not in args  # codes usually start with an int
            setupName = self.Setup.get_setup_from_Code(code=args)
            if setupName == None:
                setupName = "Unknown Setup"
            roles = convert_setup(args)
            response = self.send(f"✅ Changed setup to {setupName}")
        except Exception as e:
            print(e)
            _, setupObj = self.Setup.get_setup(args)
            code = setupObj.code
            setupName = setupObj.name
            roles = convert_setup(code)
            response = self.send(f"✅ Changed setup to {setupName}")

        if roles is None:
            response = self.send(f"⛔ Could not find/identify the setup")
            return self.response
        return [{"type": "options", "roles": roles}, response]

    @register_command("add role", isAdmin=True)
    def addrole(self, args) -> Union[Dict, List]:
        """Add a role to the setup : name, amount (default 1)"""
        args = args.split()
        if len(args) == 1:
            num, roleName = 1, args[0]
        else:
            try:
                roleName, num = get_role_count(args=args)
            except ValueError:
                return self.send(f"⛔ {args[1]} is not a valid number")
        _, roleObj = self.Role.get_role(name=roleName)
        roleID = roleObj.id

        if roleObj is None:
            return self.send(f"⛔ Could not find a role by the name {args}")

        roleName = roleObj.name
        if roleID in self.roleCache:
            self.roleCache[roleID] += num
        else:
            self.roleCache[roleID] = num
        self.response["message"] = f"✅ Added {num} {roleName} to setup"
        return [{"type": "options", "roles": self.roleCache}, self.response]

    @register_command("remove role", isAdmin=True)
    def removerole(self, args) -> Union[Dict, List]:
        """Removes a role from the setup : name, amount (default 1)"""
        args = args.split()
        if len(args) == 1:
            num, roleName = 1, args[0]
        else:
            try:
                roleName, num = get_role_count(args=args)
            except ValueError:
                response = self.send(f"⛔ {args[1]} is not a valid number")
                return self.response
        _, roleObj = self.Role.get_role(name=roleName)
        roleName = roleObj.name
        roleID = roleObj.id
        if roleObj is None:
            response = self.send(f"⛔ Could not find a role by the name {args}")
            return self.response

        if roleID in self.roleCache:
            if num < self.roleCache[roleID]:
                self.roleCache[roleID] -= num
                response = self.send(f"✅ Removed {num} {roleName} from setup")
            elif num == self.roleCache[roleID]:
                del self.roleCache[roleID]
                response = self.send(f"✅ Removed {roleName} from setup")
            elif num > self.roleCache[roleID]:
                response = self.send(
                    f"⛔ Cannot remove {num} {roleName}, there are only {self.roleCache[roleID]}"
                )
                return self.response
        return [{"type": "options", "roles": self.roleCache}, response]

    @register_command("public", isAdmin=True)
    def relist(self) -> List:
        """List the room"""
        self.isUnlisted = False
        self.response["message"] = "🦸‍♂ Made the room public"
        return [{"type": "options", "unlisted": False}, self.response]

    @register_command("private", isAdmin=True)
    def unlist(self) -> List:
        """Unlist the room"""
        self.isUnlisted = True
        self.response["message"] = "🕵️‍♀ Made the room private"
        return [{"type": "options", "unlisted": self.isUnlisted}, self.response]

    @register_command("spectate", isAdmin=True)
    def spectate(self) -> List:
        """Become a spectator"""
        return [
            {"type": "presence", "isPlayer": False},
            self.send("👀 Became a spectator"),
        ]

    @register_command("show rooms")
    def rooms(self) -> Dict:
        """List other rooms"""
        roomData = self.Room.get_rooms()
        message = f"There are {len(roomData)} rooms | {', '.join((room.name for room in roomData))}"
        return self.send(message)

    @register_command("become player", isAdmin=True)
    def player(self) -> List:
        """Become a player"""
        return [{"type": "presence", "isPlayer": True}, self.send("🎮 Became a player")]

    @register_command("rename room", isAdmin=True)
    def rename(self, name) -> List:
        """Change room name"""
        self.rname = name
        self.response["message"] = f"✅ Renamed room to {self.rname}"
        return [{"type": "options", "roomName": self.rname}, self.response]

    def _welcome(self, userID: int) -> [None, dict]:
        if userID in self.cache.data:
            return
        # If present in cache no welcome, use lru instead
        userData = self.User.get_user(userID)
        userName = userData.username
        message = f"👋 Welcome {userName}, my prefix is {self.command_prefix}"
        print(f"User joined {userName}")
        self.cache.data[userID] = userData
        return self.send(message)

    @register_command("afk check", isAdmin=True)
    def afk(self) -> List:
        """Do an AFK check"""
        return [
            {"type": "forceSpectate"},
            {"type": "presence", "isPlayer": False},
            self.send("🔁 Doing an AFK Check"),
        ]

    @register_command("ready check", isAdmin=True)
    def ready(self) -> List:
        """Do an ready check"""
        return [
            {"type": "readyCheck"},
            self.send("🔁 Doing an Ready Check"),
        ]

    @register_command("start game", isAdmin=True)
    def start(self) -> List:
        """Starts the game"""
        return [self.send("▶ Starting the game"), {"type": "startGame"}]

    @register_command("new room", isAdmin=True)
    def new(self) -> Dict:
        """Creates a new room"""
        return [self.send("Created new room"), {"type": "newGame", "roomId": None}]

    @register_command("ping")
    def ping(self) -> List:
        """Sends a ping"""
        return [{"type": "ping"}, self.send("Pong! 🏓")]

    @register_command("edit room", isAdmin=True)
    def edit(self, args) -> Union[Dict, List]: # edit room options
        """Edits the room settings. Add options to see all options"""
        args = args.split()
        if len(args) == 1:
            opt = args[0]
            exist = self.Setting.is_valid(opt)
            if exist is None or opt == "list":
                self.response["message"] = (
                    f"📜 Valid options are"
                    f" {', '.join(self.Setting.allowed_values)}"
                )
                return self.response
            else:
                if exist["allowed"] == "str":
                    self.response["message"] = (
                        f"📜 Valid options for {opt} are "
                        f"{', '.join(exist['options'])}"
                    )
                elif exist["allowed"] == "bool":
                    self.response[
                        "message"
                    ] = f"📜 Valid options for {opt} are True, False"
                else:
                    self.response[
                        "message"
                    ] = f"📜 Valid options for {opt} are between {exist['minmax'][0]} and {exist['minmax'][1]}"
                return self.response
        else:
            opt, new = args
            setting = self.Setting.edit_options(opt, new)
            if setting is None:
                self.response["message"] = (
                    f"⛔ {opt} is not a valid setting, valid options are"
                    f"{', '.join(self.Setting.allowed_values)}"
                )
                return self.response
            elif setting is False:
                exist = self.Setting.is_valid(opt)
                if exist["allowed"] == "str":
                    self.response["message"] = (
                        f"⛔ Valid options for {opt} are "
                        f"{', '.join(exist['options'])}"
                    )
                elif exist["allowed"] == "bool":
                    self.response[
                        "message"
                    ] = f"⛔ Valid options for {opt} are True, False"
                else:
                    self.response[
                        "message"
                    ] = f"📜 Valid options for {opt} are between {exist['minmax'][0]} and {exist['minmax'][1]}"
                return self.response
        self.response["message"] = f"✅ Set {opt} to {new}"
        return [self.response, setting]
