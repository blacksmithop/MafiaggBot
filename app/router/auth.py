from fastapi import APIRouter, Request
from typing import Dict
from mafiagg.credential_manager import CredentialManager
from app.utils.database import UserCollection
from app.utils.models import Login
from mafiagg.models.models import SearchUser
from uuid import uuid4

router = APIRouter()


user_db = UserCollection()

# Get player info from token (Cookie, Player ID)
# TODO: Implement dependency
@router.post("/login")
async def get_rooms(request: Request, payload: Login) -> Dict:
    login_token = uuid4().hex
    return login_token
    # cred = CredentialManager(username=payload.username, password=payload.password)
    # cookie = cred.get_cookie_data()

    # user: SearchUser = user_db.get_user(cookie=cookie)
    # user_id = user.id
    # if user_db.check_if_user_exists(user_id=user_id):
    #     return cookie
    # user_db.add_user(user_id=user.id, user_name=user.username)
    # return cookie
