from requests import get
from bs4 import BeautifulSoup
from json import dump, load
from utils.models.models import Setup
from utils.helper.decorators import getSimilarity
from collections import OrderedDict
from typing import Optional
from os import path


class GetSetup:
    BASE = "https://mafiagg.fandom.com/"
    SETUP_DIR = "./data/setups"

    def __init__(self):
        self.getSetupData()

    def getSetup(self, name: str):
        matches = {}
        name = name.title()
        response = None
        for setup in self.setups:
            score = getSimilarity(setup.name, name)
            if score > 0.7:
                matches[score] = setup
        if matches != {}:
            matches = OrderedDict(sorted(matches.items()))
            response = next(reversed(matches.items()))[1]
        description = self.formatSetupData(name=name, response=response)
        return description, response

    def getSetupByCode(self, code: str):
        match = [setup for setup in self.setups if setup.code == code]
        if len(match) > 0:
            return match[0].name
        else:
            return None

    def formatSetupData(self, name: str, response: Optional[Setup]):
        if response == None:
            text = f"❌ Could not find a setup by the name: {name}"
        else:
            text = f"✅ Role: {response.name} | Code: {response.code}"
        return text

    def getSetupData(self):
        file_path = f"{self.SETUP_DIR}/setups.json"
        if path.isfile(file_path):
            print("Loaded setups")
            with open(file_path, "r") as f:
                data = load(f)
            setups = [Setup(**item) for item in data]
            setups = sorted(setups, key=lambda x: x.name)
            self.setups = setups
        else:
            self.getTables()
            self.saveSetups()

    def saveSetups(self):
        print("Saving setups to file")
        with open("./data/setups/setups.json", "w") as f:
            dump(self.setups, f)

    def getTables(self):
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
        self.getSetupCode()

    def getSetupCode(self):
        print("Fetching setup codes")
        setups = []
        for table in self.tables:
            try:
                extracted = self.getTestedSetups(items=table)
            except Exception:
                extracted = self.getSetupFromTable(items=table)
            setups.extend(extracted)
        print(setups[0:5])
        self.setups = setups

    def getTestedSetups(self, items):
        anchors = items.find_all("a")
        print("Fetching data from URLs")
        return [
            {
                "name": anchor["title"],
                "code": self.getSetupFromUrl(f"{self.BASE}{anchor['href']}"),
            }
            for anchor in anchors
        ]

    def getSetupFromUrl(_, url):
        data = get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        print(f"Fetching data from {url}")
        try:
            code = soup.find_all("span", {"class": "copy-to-clipboard-text"})[0].text
            return code
        except:
            print("FIX")
            return None

    def getSetupFromTable(self, items):
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
