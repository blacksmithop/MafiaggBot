from fastapi import APIRouter, Request
from typing import Dict
from mafiagg.credential_manager import CredentialManager
from app.utils.database.user_db import UserCollection
from app.utils.models import Login
from mafiagg.models.models import SearchUser
from uuid import uuid4

router = APIRouter()


user_db = UserCollection()


@router.post("/login")
async def get_rooms(request: Request, payload: Login) -> Dict:

    cred = CredentialManager(username=payload.username, password=payload.password)
    cookie = cred.get_cookie_data()

    user: SearchUser = user_db.get_user(cookie=cookie)
    user_id = user.id
    if not user_db.check_if_user_exists(user_id=user_id):
        user_db.add_user(user_id=user.id, user_name=user.username)
    response = {"cookie": cookie, "user_id": user_id, "user_name": user.username}
    print(response)
    return response
