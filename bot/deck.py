from requests import Session
from json import loads, dump, load
from os import getcwd, path, mkdir
from bot.customtypes import DeckDict


class Deck:
    URL = "https://mafia.gg/api/decks"

    def __init__(self, payload, update: bool = False):
        self.json = None
        self.decks = DeckDict()
        self.loc = None
        self.create_dir()
        self.get_decks(payload, update)
        self.store_deck(update)

    def get_decks(self, payload, update):
        loc = path.join(self.loc, 'deck.json')
        if path.isfile(loc):
            print("Deck file found")
            if not update:
                return
        with Session() as s:
            num = loads(s.get(self.URL, cookies=payload).content)
        num = num['pagination']['numPages']
        print(f"Found {num} pages of decks")
        for i in range(1, num+1):
            print(f"Getting deck data {i}/12")
            with Session() as s:
                self.json = loads(s.get(f'{self.URL}?filter&page={i}', cookies=payload).content)

            for d in self.json['decks']:
                self.decks[d['name'].lower()] = d['key']

    def create_dir(self) -> None:
        self.loc = path.join(getcwd(), 'bot/data')
        try:
            mkdir(self.loc)
        except OSError:
            print("Data folder already exists")

    def store_deck(self, update) -> None:
        loc = path.join(self.loc, 'deck.json')
        if path.isfile(loc):
            if not update:
                print("Loading to memory (deck)")
                with open(loc) as f:
                    self.decks = DeckDict(load(f))
                return
        with open(loc, 'w') as f:
            dump(self.decks, f)
            print("Wrote deck data to file")

    def search_deck(self, name: str) -> [bool, str]:
        return self.decks[name.lower()]



