from fastapi import APIRouter, Request
from typing import List
from app.utils.models import ChatMessage, MessageAuthor
from app.utils.database.chat_db import ChatCollection

router = APIRouter()

chat_db = ChatCollection()


@router.post("/send_message")
async def send_message(request: Request, payload: ChatMessage):
    return chat_db.add_message_to_db(payload=payload)


@router.get("/get_recent_messages")
async def get_player_by_id(request: Request) -> List[ChatMessage]:
    return chat_db.get_latest_messages_to_user(user_id=533610)


@router.post("/get_chat_with_user")
async def get_player_by_id(
    request: Request, payload: MessageAuthor
) -> List[ChatMessage]:
    return chat_db.get_chat_between_users(
        user_a=payload.receiverId, user_b=payload.senderId
    )
