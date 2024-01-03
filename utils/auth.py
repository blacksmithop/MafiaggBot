from requests import Session
from os import getenv
from json import loads
from dotenv import load_dotenv
from utils.models.models import User

load_dotenv()


class WrongPassword(Exception):
    pass


class Cookie:
    URL = "https://mafia.gg/api/user-session"
    headers = {
        "Host": "mafia.gg",
        "Origin": "https://mafia.gg",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    

    def getCookieData(self):
        with Session() as s:
            resp = s.post(
                self.URL,
                json={
                    "login": getenv("MAFIA_GG_USERNAME"),
                    "password": getenv("MAFIA_GG_PASSWORD"),
                },
                headers=self.headers,
            )
            self.user = User(**resp.json())
            
        if resp.status_code == 401:
            raise WrongPassword("You provided incorrect password")
        self.response = loads(resp.text)
        data = resp.cookies.get_dict()
        return data
