from fastapi import APIRouter, Request
from typing import List
from app import auth
from mafiagg.room import GetRoom
from mafiagg.models.models import Room

router = APIRouter()


@router.get("/get_rooms")
async def get_rooms(request: Request) -> List[Room]:
    cookie = auth.get_cookie_data()
    room = GetRoom(cookie=cookie)
    rooms = room.get_rooms()
    return rooms
