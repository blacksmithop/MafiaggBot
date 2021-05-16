from requests import Session
from bot.customtypes import DeckDict
from os import getcwd, path, mkdir
import re
from json import dump, load


class Setup:
    URL = "https://mafiagg.fandom.com/wiki/Open_Setup_List"

    def __init__(self, update: bool = False):
        self.loc = None
        with Session() as s:
            self.data = s.get(self.URL).text
        self.setups = DeckDict()
        self.create_dir()
        self.get_setups(update)
        self.get_setup_code()
        self.store_setup(update)

    def get_setups(self, update) ->None:
        loc = path.join(self.loc, 'setup.json')
        if path.isfile(loc):
            print("Setup file found")
            if not update:
                return
        match = re.findall(r'<tr>(.*?)</tr>', self.data, re.M | re.I | re.S)
        match[:] = (i for i in match if "Player Count" not in i and "href" in i and "docs" not in i)
        for i in match:
            href, title = [x.group() for x in re.finditer(r"(?<==)('|\").*?\1(?=.*?>)", i)]
            href, title = href[1:-1], title[1:-1]
            title = title.replace("&#39;", "'").replace("&amp;", "&").replace("o&#39;", "'")
            count = re.search(r'<td>(\d+)', i).group(1)
            self.setups[title.lower()] = [
                f"https://mafiagg.fandom.com/{href}", count
            ]

    def get_setup_code(self) ->None:
        for setup in self.setups:
            print(f"Getting setup code for {setup}")
            with Session() as s:
                data = s.get(self.setups[setup][0]).text
            code = re.search(r'<div class="pi-data-value pi-font">(.*?)</div>',
                             data)
            if code:
                self.setups[setup].append(code.group(1))

    def create_dir(self) -> None:
        self.loc = path.join(getcwd(), 'bot/data')
        try:
            mkdir(self.loc)
        except OSError:
            print("Data folder already exists")

    def store_setup(self, update) -> None:
        loc = path.join(self.loc, 'setup.json')
        if path.isfile(loc):
            if not update:
                print("Loading to memory (setup)")
                with open(loc) as f:
                    self.setups = DeckDict(load(f))
                return
        with open(loc, 'w') as f:
            dump(self.setups, f)
            print("Wrote deck data to file")

    def search_setup(self, name):
        return self.setups[name.lower()]


