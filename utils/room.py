from requests import Session
from json import loads


class Room:
    URL = "https://mafia.gg/api/rooms"

    def __init__(self, payload):
        self.payload = payload

    def list_rooms(self):
        with Session() as s:
            self.json = loads(s.get(self.URL, cookies=self.payload).content)
        rooms = self.json["rooms"]
        num = len(rooms)
        lobbies = []
        if num > 0:
            lobbies = [r["name"] for r in rooms]
        return num, lobbies
