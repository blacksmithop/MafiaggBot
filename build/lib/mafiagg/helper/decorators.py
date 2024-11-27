from difflib import SequenceMatcher
from functools import wraps
from typing import Dict


def get_similar_score(a, b):
    return SequenceMatcher(None, a, b).ratio()


# ignore messages from itself
def ignore_bot_message(func):
    @wraps(func)
    def wrapper(self, payload: Dict):
        if payload["type"] == "chat":
            if "from" in payload:
                if payload["from"]["userId"] == self.botUser.id:
                    return
        res = func(self, payload)
        return res

    return wrapper


# register a command
def register_command(name: str, isAdmin: bool = False):
    def _(f):
        if not hasattr(f, "_commandName"):
            f._commandName = name
            f.isCommand = True
            f.isAdmin = isAdmin
        return f

    return _
