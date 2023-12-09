from requests import Session
from json import dump, load
from os import getcwd, path
from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from typing import List, Optional
from pathlib import Path
from auth import Cookie
from time import sleep


class Pagination(BaseModel):
    page: int
    numPages: int
    total: int

    
class Character(BaseModel):
    playerId: int
    name: str
    avatarUrl: str
    backgroundColor: str
    
class Deck(BaseModel):
    name: str
    version: int
    key: str
    builtin: bool
    deckSize: int
    uploadTimestamp: int
    sampleCharacters: List[Character]
    

class DeckData(BaseModel):
    pagination: Optional[Pagination]
    decks: List[Deck]
    

class GenerateDeck:
    URL = "https://mafia.gg/api/decks"
    DECK_DIR = "./data/decks"
    
    def __init__(self):
        self.getDecks()
            
    def updateOrCreate(self):
        self.createDeckDir()
        self.generateDeckData()
    
    def getDecks(self):
        file_path = f"{self.DECK_DIR}/decks.json"
        if path.isfile(file_path):
            print("Loading deck from file")
            with open(file_path, "r") as f:
                data = load(f)
                dataset = DeckData(**data)
                self.dataset = dataset.decks
        else:
            cookie_gen = Cookie()
            self.cookie = cookie_gen.getCookieData()
            self.updateOrCreate()

    def generateDeckData(self):
        # First we need to get the pagination data
        with Session() as sess:
            resp = sess.get(self.URL, cookies=self.cookie)
            if resp.status_code != 200:
                return
            
            data = resp.json()
            dataset = DeckData(**data)
            
        page = dataset.pagination.page
        numPages= dataset.pagination.numPages
        print(f"Page {page} of {numPages}")
        
        # Now iteratively append page data for decks 
        for page in range(2, numPages+1):
            with Session() as sess:
                print(f"Page {page} of {numPages}")
                data = sess.get(f'{self.URL}?page={page}', cookies=self.cookie).json()
                _decks = DeckData(**data).decks
                dataset.decks.extend(_decks)
                sleep(1.5)
                
        dataset.pagination.page = page
        self.dataset = dataset
        self.storeDeck()
        self.dataset = dataset.decks
        
    def createDeckDir(self) -> None:
        Path(self.DECK_DIR).mkdir(parents=True, exist_ok=True)

    def storeDeck(self) -> None:
        with open(f"{self.DECK_DIR}/decks.json", "w") as f:
            data = self.dataset.model_dump(mode='json')
            dump(data, f, indent=4, sort_keys=True, default=str)
            print("Saved deck data to file")

    def search(self, name: str) -> [bool, str]:
        gen = (item for item in self.dataset if item.name.lower() == name.lower())
        return next(gen, None)

if __name__ == "__main__":
    deck = GenerateDeck()
    print(deck.search(name="Phighting!"))


