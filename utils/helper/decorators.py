from difflib import SequenceMatcher
from functools import wraps
from typing import Dict


def getSimilarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# ignore messages from itself
def ignoreBotMessage(func):
    @wraps(func)
    def wrapper(self, payload: Dict):
        if payload["type"] == "chat":
            if "from" in payload:
                if payload["from"]["userId"] == self.botUser.id:
                    return
        res = func(self, payload)
        return res

    return wrapper


# owner only commands
def isOwnerOnly(func):
    @wraps(func)
    def wrapper(self, payload: Dict):
        if payload["type"] == "chat":
            if "from" in payload:
                if payload["from"]["userId"] not in self.ALLOWED:
                    return
        res = func(self, payload)
        return res

    return wrapper


# register a command
def registerCommand(v):
    def _(f):
        if not hasattr(f, "_commandName"):
            f._commandName = v
            f.isCommand = True
        return f

    return _
