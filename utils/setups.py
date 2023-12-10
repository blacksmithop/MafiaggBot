from requests import get
from bs4 import BeautifulSoup


class GenerateSetup:
    BASE = "https://mafiagg.fandom.com/"
    
    def getTables(self):
        print("Fetching setup metadata")
        data = get(f"{self.BASE}/Open_Setup_List")
        soup = BeautifulSoup(data.text)
        self.headers = [header.text[:-3] for header in soup.find_all(['h2', 'h3']) if 'Setup' in header.text]
        self.tables = soup.find_all('table')[:4]

    def getSetupCode(self):
        print("Fetching setup codes")
        self.setups = {
            self.headers[0]: self.getTestedSetups(anchors=self.tables[0].find_all('a')),
            self.headers[1]: self.getTestedSetups(anchors=self.tables[1].find_all('a')),
            self.headers[2]: self.getSetupFromTable(self.tables[2]),
            self.headers[3]: self.getTestedSetups(anchors=self.tables[3].find_all('a'))
        }
    
    def getTestedSetups(self, anchors):
        print("Fetching data from URLs")
        return [
            {
                "name": anchor["title"], "code": self.getSetupFromUrl(url=f"{self.BASE}{anchor['href']}")
            } for anchor in anchors
        ]    
        
    def getSetupFromUrl(url: str):
        data = get(url)
        soup = BeautifulSoup(data.text)
        code = soup.find_all("span", {"class": "copy-to-clipboard-text"})[0].text
        print(f"Fetching data from {url}")
        return code
            
    def getSetupFromTable(self, items):
        print("Fetching data from table")
        return [
            {
                "name": item.find_all('td')[1].text.rstrip(), "code": item.find_all('td')[-1].text.rstrip()
            } for item in items
        ]