from requests import Session
from json import dump, load
from os import path
from pathlib import Path
from mafiagg.helper.decorators import get_similar_score
from time import sleep
from mafiagg.models.models import DeckData, Deck
from typing import Optional


class GetDeck:
    URL = "https://mafia.gg/api/decks"
    RANDOM_URL = "https://mafia.gg/api/decks-random-key"
    DECK_DIR = "./data/decks"

    def __init__(self, cookie):
        self.cookie = cookie
        self.get_decks()

    def download_deck(self):
        self.create_deck_dir()
        self.generate_deck_data()

    def get_decks(self):
        file_path = f"{self.DECK_DIR}/decks.json"
        if path.isfile(file_path):
            print("Loaded decks")
            with open(file_path, "r") as f:
                data = load(f)
                dataset = DeckData(**data)
                self.dataset = dataset.decks
        else:
            self.download_deck()

    def generate_deck_data(self):
        # First we need to get the pagination data
        print("Fetching pagination data for deck")
        with Session() as sess:
            resp = sess.get(self.URL, cookies=self.cookie)
            if resp.status_code != 200:
                return

            data = resp.json()
            dataset = DeckData(**data)
        page = dataset.pagination.page
        numPages = dataset.pagination.numPages
        print(f"Getting data page {page} of {numPages}")

        # Now iteratively append page data for decks
        for page in range(2, numPages + 1):
            with Session() as sess:
                print(f"Page {page} of {numPages}")
                data = sess.get(f"{self.URL}?page={page}", cookies=self.cookie).json()
                _decks = DeckData(**data).decks
                dataset.decks.extend(_decks)
                sleep(1.5)

        dataset.pagination.page = page
        self.dataset = dataset
        self.store_deck()
        self.dataset = dataset.decks

    def create_deck_dir(self) -> None:
        Path(self.DECK_DIR).mkdir(parents=True, exist_ok=True)

    def store_deck(self) -> None:
        with open(f"{self.DECK_DIR}/decks.json", "w") as f:
            data = self.dataset.model_dump(mode="json")
            dump(data, f, indent=4, sort_keys=True, default=str)
            print("Saved deck data to file")

    def get_deck(self, name: str, format=True) -> Optional[Deck]:
        gen = (
            item
            for item in self.dataset
            if get_similar_score(item.name.lower(), name.lower()) > 0.6
        )
        response = next(gen, None)
        if format:
            deckData = self.format_deck(name=name, response=response)
            return deckData
        else:
            return response

    def get_deck_by_id(self, id: str) -> Deck:
        gen = (item for item in self.dataset if item.key == id)
        response = next(gen, None)
        return response

    def get_random_deck(self) -> str:
        with Session() as sess:
            resp = sess.get(self.RANDOM_URL, cookies=self.cookie)
            if resp.status_code != 200:
                return
            return resp.json()["key"]

    def format_deck(self, name: str, response: Optional[Deck]):
        if response == None:
            text = f"❌ Could not find a deck by the name: {name}"
        else:
            text = f"✅ Deck: {response.name} | Size: {response.deckSize} | Version: {response.version}"
        return text


if __name__ == "__main__":
    deck = GetDeck()
    print(deck.search(name="Phighting!"))
