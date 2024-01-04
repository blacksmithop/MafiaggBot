from difflib import SequenceMatcher
from functools import wraps
from typing import Dict


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def ignore_bot_message(func):
    @wraps(func)
    def wrapper(self, payload: Dict):
        if payload["type"] == "chat":
            if "from" in payload:
                if payload["from"]["userId"] == self.id:
                    return
        res = func(self, payload)
        return res

    return wrapper


def register_command(v):
    def _(f):
        if not hasattr(f, '_commandName'):
            f._commandName = v
            f.isCommand = True
        return f
    return _

def isBotCommand(data):
    name, cmd = data
    return name[:2] != "__" and hasattr(cmd, "isCommand")


def convertSetup(roles: str) -> dict:
    try:
        # noinspection PyTypeChecker
        return dict(map(lambda x: str.split(x, "a"), str.split(roles, "b")))
    except ValueError:
        pass

def commandNotFound():
    return None