from requests import Session
from json import dump, load
from os import getcwd, path
from bot.customtypes import DeckDict
from pydantic import BaseModel, validator
from datetime import datetime
from typing import List
from pathlib import Path

class Pagination(BaseModel):
    page: int
    numPages: int
    total: int

    
class Character(BaseModel):
    playedId: int
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
    
    @validator("uploadTimestamp", pre=True)
    def uploadTimestamp_validate(cls, uploadTimestamp):
        return datetime.fromtimestamp(uploadTimestamp)

class DeckData(BaseModel):
    pagination: Pagination
    decks: List[Deck]
    

class GenerateDeck:
    URL = "https://mafia.gg/api/decks"
    DECK_DIR = "./data/decks/deck.json"
    
    def __init__(self, update: bool = False):
        self.getDecks(update)
            
    def updateOrCreate(self, update: bool):
        self.createDeckDir()
        self.generateDeckData()
    
    def getDecks(self, update: bool):
        if path.isfile(self.DECK_DIR) and not update:
            print("Loading to memory (deck)")
            with open(self.DECK_DIR) as f:
                data = load(f)
                dataset = DeckData(**data)
                self.dataset = dataset.decks
        else:
            self.updateOrCreate()

    def generateDeckData(self):
        # First we need to get the pagination data
        with Session() as sess:
            resp = sess.get(self.URL)
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
                data = sess.get(f'{self.URL}?page={page}').json()
                _decks = DeckData(**data).decks
                dataset.decks.extend(_decks)

        dataset.pagination.page = page
        self.store_deck()
        self.dataset = dataset.decks
        
    def createDeckDir(self) -> None:
        Path(self.DECK_DIR).mkdir(parents=True, exist_ok=True)

    def store_deck(self) -> None:
        with open(self.DECK_DIR, 'w') as f:
            dataset = dict(self.dataset)
            dump(dataset, f)
            print("Saved deck data to file")

    def search(self, name: str) -> [bool, str]:
        return next(item for item in self.dataset if item.name.lower() == name)



