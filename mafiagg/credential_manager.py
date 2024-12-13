from requests import Session
from os import getenv
from json import loads
from mafiagg.models.models import User
from mafiagg.helper.custom_exceptions import WrongPassword
from typing import Optional




class CredentialManager:
    URL = "https://mafia.gg/api/user-session"
    headers = {
        "Host": "mafia.gg",
        "Origin": "https://mafia.gg",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }

    def __init__(
        self, username: Optional[str] = None, password: Optional[str] = None
    ) -> None:
        if username == None and password == None:
            self.credentials = {  # load from .env file
                "login": getenv("MAFIA_USERNAME"),
                "password": getenv("MAFIA_PASSWORD"),
            }
        else:
            self.credentials = {"login": username, "password": password}

        self.login()

    def login(self):
        with Session() as s:
            try:
                resp = s.post(
                    self.URL,
                    json=self.credentials,
                    headers=self.headers,
                )

                if resp.status_code == 401:
                    raise WrongPassword("Provided username/password is incorrect")
                self.user = User(**resp.json())

                self.cookies = resp.cookies.get_dict()
            except Exception as e:
                print(f"Failed to login due to {e}")
                self.cookies = {}

    def logout(self):
        with Session() as s:
            resp = s.delete(
                self.URL,
                json=self.credentials,
                headers=self.headers,
            )
            print("Logged out successfully")

    def get_cookie_data(self):
        return self.cookies

    def get_user(self):
        return self.user
