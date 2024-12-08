from fastapi import APIRouter, Request
from typing import Dict
from mafiagg.credential_manager import CredentialManager
from pydantic import BaseModel


router = APIRouter()

class Login(BaseModel):
    username: str
    password: str


@router.post("/login")
async def get_rooms(request: Request, payload: Login) -> Dict:
    cred = CredentialManager(username=payload.username, password=payload.password)
    cookies = cred.get_cookie_data()
    return cookies