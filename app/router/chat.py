from fastapi import APIRouter, Request
from typing import List, Union

router = APIRouter()


@router.get("/chat/load_chat")
async def get_player_by_id(request: Request, player_id: int) -> List:
    return []