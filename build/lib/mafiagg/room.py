from requests import Session
from mafiagg.models.models import Room


class GetRoom:
    URL = "https://mafia.gg/api/rooms"

    def __init__(self, cookie):
        self.cookie = cookie
        self.rooms = []

    def get_rooms(self):
        with Session() as s:
            resp = s.get(self.URL, cookies=self.cookie)
            data = resp.json()
        rooms = data["rooms"]
        self.rooms = [Room(**item) for item in rooms]
        return self.rooms


if __name__ == "__main__":
    r = get_rooms()
    print(r.get_rooms())
