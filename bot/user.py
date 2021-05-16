from requests import Session
from bot.customtypes import WrongPassword
from os import getenv
from json import loads
try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    print("Dotenv not installed\nChecking environment variables")


class User:
    URL = "https://mafia.gg/api/user-session"

    def __init__(self):
        with Session() as s:
            cookie = s.post(self.URL, json={'login': getenv('USER'), 'password': getenv('PASS')})
        if cookie.status_code == 401:
            raise WrongPassword("You provided incorrect password")
        self.response = loads(cookie.text)
        self.cookie = cookie.cookies.get_dict()
