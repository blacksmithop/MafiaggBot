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
