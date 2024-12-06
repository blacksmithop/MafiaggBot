from mafiagg.models.models import SearchUser
from requests import Session


class GetUser:
    def get_user(self, id: str):
        with Session() as s:
            res = s.get(f"https://mafia.gg/api/users/{id}").json()
        if len(res) == 0:
            return None
        res = res[0]
        user = SearchUser(**res)
        return user
