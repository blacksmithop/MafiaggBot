class DeckDict(dict):
    def __missing__(self, key):
        for k in self.keys():
            if key in k:
                return self[k]


class WrongPassword(Exception):
    pass
