from requests import Session
from os import getenv
from json import loads
from dotenv import load_dotenv
from utils.models.models import User
from utils.helper.custom_exceptions import WrongPassword
from typing import Optional


load_dotenv()


class CredentialManager:
    URL = "https://mafia.gg/api/user-session"
    headers = {
        "Host": "mafia.gg",
        "Origin": "https://mafia.gg",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }

    def __init__(self, username: Optional[str] = None, password: Optional[str] = None) -> None:
        if username == None and password == None:
            credentials = { # load from .env file
                "login": getenv("MAFIA_USERNAME"),
                "password": getenv("MAFIA_PASSWORD"),
            }
        else:
            credentials = {
                "login": username,
                "password": password
            }
        with Session() as s:
            resp = s.post(
                self.URL,
                json=credentials,
                headers=self.headers,
            )
            self.user = User(**resp.json())

        if resp.status_code == 401:
            raise WrongPassword("Provided username/password is incorrect")
        
        self.cookies = resp.cookies.get_dict()

    def getCookieData(self):
        return self.cookies
    
    def getUser(self):
        return self.user
