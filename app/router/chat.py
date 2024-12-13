from fastapi import APIRouter, Request
from typing import List
from app.utils.models import ChatMessage
from datetime import datetime


router = APIRouter()


messages = [
    ChatMessage(
        id="ds2d23", sender="Bob", content="Hi", timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), type="text"
    ),
    ChatMessage(
        id="dsdsd23",
        sender="Alice",
        content="Hello",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        type="text",
    ),
    ChatMessage(
        id="dsd2d23",
        sender="Jerry",
        content="Hey there",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        type="text",
    ),
    ChatMessage(
        id="dsdds423",
        sender="Phil",
        content="How are you",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        type="text",
    ),
]


@router.get("/load_chat_messages")
async def get_player_by_id(request: Request) -> List[ChatMessage]:
    return messages
