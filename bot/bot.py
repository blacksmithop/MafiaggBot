from json import loads
from bot.deck import Deck
from bot.role import Role
from bot.build import Setup
from bot.setting import Setting
from typing import Union
from requests import Session
from inspect import getmembers, isfunction


def not_found():
    return None


class UserCache:
    data = dict()


class Bot:
    def __init__(self, user, _id):
        self.prefix = "$"
        self._deck = Deck(user)
        self._role = Role()
        self._setup = Setup()
        self._setting = Setting()
        self.id = _id
        self.response = {'type': 'chat', 'message': "Couldn't parse command"}
        self.rname, self.unlisted = None, None
        self.cache = UserCache()
        self.roles = dict()

    def reset_cache(self):
        self.cache.data = dict()

    def parse(self, payload: dict) -> Union[dict, None]:
        if payload['type'] == 'chat':
            if 'from' in payload:
                if payload['from']['userId'] == self.id:
                    return
            msg = payload['message']
            if msg[0] != self.prefix:
                return
            cmd, args = self.parse_command(msg[1:])
            cmd = self.get_command(cmd)
            if callable(cmd) and cmd.__doc__:
                if args is not None:
                    data = cmd(args)
                else:
                    try:
                        data = cmd()
                    except TypeError:
                        self.response['message'] = f"✅ Command [{cmd.__name__}] : {cmd.__doc__}"
                        return self.response
                return data
            else:
                return
        elif payload['type'] == 'userJoin':
            print(payload)
            return self._welcome(payload['userId'])
        else:
            return

    @staticmethod
    def parse_command(msg: str) -> list:
        msg = msg.split(' ')
        if len(msg) == 2:
            cmd, args = msg
        elif len(msg) >= 3:
            cmd, args = msg[0], msg[1:]
            args = ' '.join(args)
        else:
            cmd, args = msg[0], None
        return [cmd, args]

    def get_command(self, cmd_name: str):
        fn = getattr(self, cmd_name, not_found())
        return fn

    def deck(self, args) -> dict:
        """ Search for a deck (name) """
        _id = self._deck.search_deck(args)
        if _id is None:
            self.response['message'] = f"⛔ Could not find a deck by the name {args}"
        else:
            self.response['message'] = f"✅ The ID for {args} deck is {_id}"
        return self.response

    def role(self, args) -> dict:
        """ Search for a role (name) """
        _id = self._role.get_role(args)
        if _id is None:
            self.response['message'] = f"⛔ Could not find a role by the name {args}"
        else:
            self.response['message'] = f"✅ The ID for {args} is {_id}"
        return self.response

    def setup(self, args) -> dict:
        """ Search for a setup (name) """

        res = self._setup.search_setup(args)
        if res is None:
            self.response['message'] = f"⛔ Could not find a setup by the name {args}"
        else:
            url, size, code = res
            args = f"""
                    ID: {code}
                    Players: {size}
                    Wiki: {url}
                    """
            self.response['message'] = args
        return self.response

    def usesetup(self, args) -> [dict, list]:
        """ Change the current setup (give name)"""
        res = self._setup.search_setup(args.lower())
        if res is None:
            self.response['message'] = f"⛔ Could not find a setup by the name {args}"
            return self.response
        self.response['message'] = f"✅ Set setup to {args}"
        url, cnt, _id = res
        roles = convertSetup(_id)
        self.roles = roles
        if roles is None:
            self.response['message'] = f"⛔ Could not convert {_id} to roles"
            return self.response
        return [{'type': 'options', 'roles': roles},
                self.response]

    def addrole(self, args) -> [dict, list]:
        """Add a role to the setup : name, amount(default=1)"""
        args = args.split()
        if len(args) == 1:
            num, role = 1, args[0]
        else:
            try:
                role, num = args[0], int(args[1])
            except ValueError:
                self.response['message'] = f"⛔ {args[1]} is not a valid number"
                return self.response
        _id = self._role.get_role(role.lower())
        if _id is None:
            self.response['message'] = f"⛔ Could not find a role by the name {args}"
            return self.response
        if _id in self.roles:
            self.roles[_id] += num
        else:
            self.roles[_id] = num
        self.response['message'] = f"✅ Added {num} {role} to setup"
        return [{'type': 'options', 'roles': self.roles},
                self.response]

    def removerole(self, args) -> [dict, list]:
        """Removes a role from the setup : name, amount(default=1)"""
        args = args.split()
        if len(args) == 1:
            num, role = 1, args[0]
        else:
            try:
                role, num = args[0], int(args[1])
            except ValueError:
                self.response['message'] = f"⛔ {args[1]} is not a valid number"
                return self.response
        _id = self._role.get_role(role.lower())
        if _id is None:
            self.response['message'] = f"⛔ Could not find a role by the name {args}"
            return self.response
        if _id in self.roles:
            if num < self.roles[_id]:
                self.roles[_id] -= num
                self.response['message'] = f"✅ Removed {num} {role} from setup"
            elif num == self.roles[_id]:
                del self.roles[_id]
                self.response['message'] = f"✅ Removed {role} from setup"
            elif num > self.roles[_id]:
                self.response['message'] = f"⛔ Cannot remove {num} {role}, there are only {self.roles[_id]}"
                return self.response
            return [{'type': 'options', 'roles': self.roles},
                    self.response]

    def relist(self) -> list:
        """ List the room """
        self.unlisted = False
        self.response['message'] = "🦸‍♂ Relisted the room"
        return [{'type': 'options', 'unlisted': False},
                self.response]

    def unlist(self) -> list:
        """ Unlist the room """
        self.unlisted = True
        self.response['message'] = "🕵️‍♀ Unlisted the room"
        return [{'type': 'options', 'unlisted': self.unlisted},
                self.response]

    def spectate(self) -> list:
        """ Become a spectator """
        self.response['message'] = "👀 Became a spectator"
        return [{'type': 'presence', 'isPlayer': False},
                self.response]

    def player(self) -> list:
        """ Become a player """
        self.response['message'] = "🎮 Became a player"
        return [{'type': 'presence', 'isPlayer': True},
                self.response]

    def rename(self, name) -> list:
        """ Change room name """
        self.rname = name
        self.response['message'] = f"✅ Renamed room to {self.rname}"
        return [{'type': 'options', 'roomName': self.rname},
                self.response]

    def setcode(self, args) -> [dict, list]:
        """ Change the current setup (give ID)"""
        roles = convertSetup(args.strip())
        if roles is None:
            self.response['message'] = f"⛔ Couldn't convert {args} to roles"
            return self.response
        self.response['message'] = f"✅ Set setup to {args}"
        return [{'type': 'options', 'roles': roles},
                self.response]

    def setdeck(self, args) -> [dict, list]:
        """ Change the current deck (give name)"""
        _id = self._deck.search_deck(args)
        if not _id:
            self.response['message'] = f"⛔ Could not find a deck with the name {args}"
            return self.response
        self.response['message'] = f"✅ Set deck to {args}"
        return [{'type': 'options', 'deck': _id},
                self.response]

    def _welcome(self, _id: int) -> [None, dict]:
        if _id in self.cache.data:
            return
        # If present in cache no welcome, use lru instead
        with Session() as s:
            res = loads(s.get(f"https://mafia.gg/api/users/{_id}").text)
        self.response['message'] = f"👋 Welcome {res[0]['username']}, my prefix is {self.prefix}"
        self.cache.data[_id] = res[0]['username']
        return self.response

    def afk(self) -> list:
        """ Do an AFK check """
        self.response['message'] = f"🔁 Doing an AFK Check"
        return [{"type": "forceSpectate"}, {'type': 'presence', 'isPlayer': False},
                self.response]

    def start(self) -> list:
        """ Start the game """
        self.response['message'] = f"▶ Starting the game"
        return [{"type": "startGame"},
                self.response]

    @staticmethod
    def new() -> dict:
        """ Creates a new room """
        return {'type': 'newGame', 'roomId': None}

    def help(self, args=None) -> dict:
        """ Shows the help command """
        fn = getmembers(Bot, isfunction)
        if args is None:
            fn = list(filter(lambda x: x[1].__doc__, fn))
            fn[:] = (i[0] for i in fn)
            fn: list
            self.response[
                'message'] = f"Commands are {', '.join(fn)} GitHub: https://github.com/blacksmithop/mafiaggbot"
            return self.response
        fn = list(filter(lambda x: x[0] == args, fn))
        if not fn:
            self.response['message'] = f"⛔ No command named [{args}]"
        else:
            self.response['message'] = f"✅ Command [{fn[0][0]}] : {fn[0][1].__doc__}"
        return self.response

    def ping(self) -> list:
        """ Sends a ping """
        self.response['message'] = "Pong! 🏓"
        return [
            {"type": "ping"}, self.response
        ]

    def edit(self, args)->[dict, list]:
        """ Edits the room settings, See $edit list for all"""
        args = args.split()
        if len(args) == 1:
            opt = args[0]
            exist = self._setting.is_valid(opt)
            if exist is None or opt == "list":
                self.response['message'] = f"📜 Valid options are" \
                                           f" {', '.join(list(self._setting.edits.keys()))}"
                return self.response
            else:
                if exist['allowed'] == "str":
                    self.response['message'] = f"📜 Valid options for {opt} are " \
                                               f"{', '.join(exist['options'])}"
                elif exist["allowed"] == "bool":
                    self.response['message'] = f"📜 Valid options for {opt} are True, False"
                else:
                    self.response['message'] = f"📜 Valid options for {opt} are between {exist['minmax'][0]} and {exist['minmax'][1]}"
                return self.response
        else:
            opt, new = args
            setting = self._setting.edit_option(opt, new)
            if setting is None:
                self.response['message'] = f"⛔ {opt} is not a valid setting, valid options are" \
                                           f"{', '.join(list(self._setting.edits.keys()))}"
                return self.response
            elif setting is False:
                exist = self._setting.is_valid(opt)
                if exist['allowed'] == "str":
                    self.response['message'] = f"⛔ Valid options for {opt} are " \
                                               f"{', '.join(exist['options'])}"
                elif exist['allowed'] == "bool":
                    self.response['message'] = f"⛔ Valid options for {opt} are True, False"
                else:
                    self.response['message'] = f"📜 Valid options for {opt} are between {exist['minmax'][0]} and {exist['minmax'][1]}"
                return self.response
        self.response['message'] = f"✅ Set {opt} to {new}"
        return [self.response, setting]


def convertSetup(roles: str) -> dict:
    try:
        # noinspection PyTypeChecker
        return dict(map(lambda x: str.split(x, 'a'), str.split(roles, 'b')))
    except ValueError:
        pass
