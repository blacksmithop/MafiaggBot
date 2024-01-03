from requests import Session
from json import loads
from utils.auth import Cookie
from utils.models.models import Room


class GetRooms:
    URL = "https://mafia.gg/api/rooms"

    def __init__(self):
        cookie_gen = Cookie()
        self.cookie = cookie_gen.getCookieData()
        self.rooms = []
        
    def getRooms(self):
        with Session() as s:
            resp = s.get(self.URL, cookies=self.cookie)
            data = resp.json()
        rooms = data["rooms"]
        self.rooms = [Room(**item) for item in rooms]
        return self.rooms
    
if __name__ == "__main__":
    r = GetRooms()
    print(r.getRooms())