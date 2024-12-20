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
    get_role_name_and_count,
)
from mafiagg.credential_manager import CredentialManager
from mafiagg.bot.botbase import BotBase
from typing import Dict, List, Optional, Union
from mafiagg.chatbot.chat import get_bot_response


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
        self.role_cache = {}  # TODO: Improve
        self.register_bot_commands()
        self.register_modules()

    def register_modules(self):
        self.Role = GetRole()
        self.Deck = GetDeck(cookie=self.cookie)
        self.User = GetUser(cookie=self.cookie)
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
            user_id = payload["from"]["userId"]

            if msg[0] != self.command_prefix:
                try:
                    bot_message = get_bot_response(user_query=msg, user_id=user_id)
                    if bot_message:
                        return {"type": "chat", "message": f"[AI] {bot_message}"}
                except Exception as e:
                    print(f"Could not chat with user {user_id}, Error:\n{e}")
                return
            cmd, args = self.parse_command(msg[1:])
            if cmd == None:
                pass
            if (
                hasattr(cmd, "isAdmin")
                and cmd.isAdmin
                and user_id not in self.admin_users
            ):  # TODO: Keep track of user (history)
                return {
                    "type": "chat",
                    "message": "❌ You do not have permission to run this command",
                }

            # cmd = self.get_command(cmd)
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
        """Search for a deck | {prefix}{cmd} deck-name"""
        deckData = self.Deck.get_deck(args)
        self.response["message"] = deckData
        return self.response

    @register_command("use deck", isAdmin=True)
    def usedeck(self, args) -> Union[Dict, List]:
        """Change the current deck | {prefix}{cmd} deck-name"""
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
        """Search for a role | {prefix}{cmd} role-name"""
        roleData, _ = self.Role.get_role(role_name=args)
        self.response["message"] = roleData
        return self.response

    @register_command("get setup")
    def setup(self, args) -> Dict:
        """Search for a setup | {prefix}{cmd} setup-name"""
        setupData, _ = self.Setup.get_setup(args)
        self.response["message"] = setupData
        return self.response

    @register_command("use setup", isAdmin=True)
    def usesetup(self, args) -> Union[Dict, List]:
        """Change the current setup | {prefix}{cmd} setup-name"""
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
        """Add a role to the setup | {prefix}{cmd} role-name amount(1)"""
        args = args.split()
        if len(args) == 1:
            role_count, role_name = 1, args[0]
        else:
            try:
                role_name, role_count = get_role_name_and_count(args=args)
                if role_count < 1:
                    return self.send(f"⛔ Role count {args[1]} should be greater than 0")
            except ValueError:
                return self.send(f"⛔ Role count cannot accept {args[1]}")
        _, selected_role = self.Role.get_role(role_name=role_name)

        if selected_role is None:
            return self.send(f"⛔ Could not find a role by the name {role_name}")

        role_id = selected_role.id

        role_name = selected_role.name
        if role_id in self.role_cache:
            self.role_cache[role_id] += role_count
        else:
            self.role_cache[role_id] = role_count
        self.response["message"] = f"✅ Added {role_count} {role_name} to setup"
        return [{"type": "options", "roles": self.role_cache}, self.response]

    @register_command("remove role", isAdmin=True)
    def removerole(self, args) -> Union[Dict, List]:
        """Removes a role from the setup | {prefix}{cmd} role-name amount(1)"""
        args = args.split()
        if len(args) == 1:
            role_count, role_name = 1, args[0]
        else:
            try:
                role_name, role_count = get_role_name_and_count(args=args)
            except ValueError:
                return self.send(f"⛔ {args[1]} is not a valid number")
        _, selected_role = self.Role.get_role(role_name=role_name)
        role_name = selected_role.name
        if selected_role is None:
            return self.send(f"⛔ Could not find a role by the name {args}")

        role_id = selected_role.id

        if role_id in self.role_cache:
            if role_count < self.role_cache[role_id]:
                self.role_cache[role_id] -= role_count
                response = self.send(f"✅ Removed {role_count} {role_name} from setup")
            elif role_count == self.role_cache[role_id]:
                del self.role_cache[role_id]
                response = self.send(f"✅ Removed {role_name} from setup")
            elif role_count > self.role_cache[role_id]:
                response = self.send(
                    f"⛔ Cannot remove {role_count} {role_name}, there are only {self.role_cache[role_id]}"
                )
                return self.response
        return [{"type": "options", "roles": self.role_cache}, response]

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
        room_data = self.Room.get_rooms()
        if len(room_data) == 0:
            message = "There are no rooms"
        else:
            message = f"There are {len(room_data)} rooms | {', '.join((room.name for room in room_data))}"
        return self.send(message)

    @register_command("join", isAdmin=True)
    def player(self) -> List:
        """Become a player"""
        return [{"type": "presence", "isPlayer": True}, self.send("🎮 Became a player")]

    @register_command("rename room", isAdmin=True)
    def rename(self, name) -> List:
        """Change room name"""
        self.rname = name
        self.response["message"] = f"✅ Renamed room to {self.rname}"
        return [{"type": "options", "roomName": self.rname}, self.response]

    def _welcome(self, user_id: int) -> Optional[dict]:
        if user_id in self.cache.data:
            return
        # TODO: Add user to cache/db
        userData = self.User.get_user(user_id)
        user_name = userData.username

        message = f"Welcome {user_name}👋! My prefix is {self.command_prefix}"
        # This is the fallback

        greet_user_query = f"Say a short witty greeting for a person named {user_name}"
        # TODO: Custom chain/tool for greeting

        try:
            bot_message = get_bot_response(user_query=greet_user_query, user_id=user_id)
            if bot_message:
                message = f"[AI] {bot_message}. My prefix is {self.command_prefix}"
        except Exception as e:
            print(f"Failed to send greeting due to {str(e)}")

        print(f"User joined: {user_name}")
        self.cache.data[user_id] = userData
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
    def edit(self, args) -> Union[Dict, List]:  # edit room options
        """Edits the room settings. Add options to see all options"""
        args = args.split()
        if len(args) == 1:
            opt = args[0]
            exist = self.Setting.is_valid(opt)
            if exist is None or opt == "list":
                self.response["message"] = (
                    f"📜 Valid options are" f" {', '.join(self.Setting.allowed_values)}"
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
