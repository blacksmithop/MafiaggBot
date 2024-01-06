from requests import get
from bs4 import BeautifulSoup
from json import dump, load
from utils.models.models import Setup
from utils.helper.decorators import get_similar_score
from collections import OrderedDict
from typing import Optional
from os import path


class GetSetup:
    BASE = "https://mafiagg.fandom.com/"
    SETUP_DIR = "./data/setups"

    def __init__(self):
        self.load_setup()

    def get_setup(self, name: str):
        matches = {}
        name = name.title()
        response = None
        for setup in self.setups:
            score = get_similar_score(setup.name, name)
            if score > 0.7:
                matches[score] = setup
        if matches != {}:
            matches = OrderedDict(sorted(matches.items()))
            response = next(reversed(matches.items()))[1]
        description = self.format_setup(name=name, response=response)
        return description, response

    def get_setup_from_Code(self, code: str):
        match = [setup for setup in self.setups if setup.code == code]
        if len(match) > 0:
            return match[0].name
        else:
            return None

    def format_setup(self, name: str, response: Optional[Setup]):
        if response == None:
            text = f"❌ Could not find a setup by the name: {name}"
        else:
            text = f"✅ Role: {response.name} | Code: {response.code}"
        return text

    def load_setup(self):
        file_path = f"{self.SETUP_DIR}/setups.json"
        if path.isfile(file_path):
            print("Loaded setups")
            with open(file_path, "r") as f:
                data = load(f)
            setups = [Setup(**item) for item in data]
            setups = sorted(setups, key=lambda x: x.name)
            self.setups = setups
        else:
            self.get_tables()
            self.save_setup()

    def save_setup(self):
        print("Saving setups to file")
        with open("./data/setups/setups.json", "w") as f:
            dump(self.setups, f)

    def get_tables(self):
        print("Fetching setup metadata")
        data = get(f"{self.BASE}/Open_Setup_List")
        soup = BeautifulSoup(data.text, "html.parser")
        self.headers = [
            header.text[:-3]
            for header in soup.find_all(["h2", "h3"])
            if "Setup" in header.text
        ]
        self.tables = soup.find_all("table")
        self.tables = [table for table in self.tables][:4]
        self.get_setupCode()

    def get_setupCode(self):
        print("Fetching setup codes")
        setups = []
        for table in self.tables:
            try:
                extracted = self.get_tested_setup(items=table)
            except Exception:
                extracted = self.get_setup_from_table(items=table)
            setups.extend(extracted)
        print(setups[0:5])
        self.setups = setups

    def get_tested_setup(self, items):
        anchors = items.find_all("a")
        print("Fetching data from URLs")
        return [
            {
                "name": anchor["title"],
                "code": self.get_setup_from_url(f"{self.BASE}{anchor['href']}"),
            }
            for anchor in anchors
        ]

    def get_setup_from_url(_, url):
        data = get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        print(f"Fetching data from {url}")
        try:
            code = soup.find_all("span", {"class": "copy-to-clipboard-text"})[0].text
            return code
        except:
            print("FIX")
            return None

    def get_setup_from_table(self, items):
        print("Fetching data from table")
        setups = []

        for item in items:
            try:
                entry = {
                    "name": item.find_all("td")[1].text.rstrip(),
                    "code": item.find_all("td")[-1].text.rstrip(),
                }
                setups.append(entry)
            except AttributeError:
                continue
        return setups


if __name__ == "__main__":
    setup = GenerateSetup()
