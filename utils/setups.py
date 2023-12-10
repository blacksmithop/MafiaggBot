from requests import get
from bs4 import BeautifulSoup
from json import dump

class GenerateSetup:
    BASE = "https://mafiagg.fandom.com/"
    
    def __init__(self):
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
        self.headers = [header.text[:-3] for header in soup.find_all(['h2', 'h3']) if 'Setup' in header.text]
        self.tables = soup.find_all('table')
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
        anchors = items.find_all('a')
        print("Fetching data from URLs")
        return [
            {
                "name": anchor["title"], "code": self.getSetupFromUrl(f"{self.BASE}{anchor['href']}")
            } for anchor in anchors
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
                    "name": item.find_all('td')[1].text.rstrip(), "code": item.find_all('td')[-1].text.rstrip()
                } 
                setups.append(entry)
            except AttributeError:
                continue
        return setups
        
if __name__ == "__main__":
    setup = GenerateSetup()