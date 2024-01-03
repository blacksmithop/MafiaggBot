from utils.models.models import User
from requests import Session

class GetUser:
    def getUser(self, id: str):
        with Session() as s:
            res = s.get(f"https://mafia.gg/api/users/{id}").json()
        if len(res) == 0:
            return None
        res = res[0]
        user = User(**res)
        return user