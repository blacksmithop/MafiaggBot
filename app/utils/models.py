from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional


class Login(BaseModel):
    username: str
    password: str


class PlayerStats(BaseModel):
    user_id: int
    username: str
    createdAt: str
    totalGames: int = 1
    winRate: int = 0
    townWinRate: int = 0
    mafiaWinRate: int = 0
    neutralWinRate: int = 0


class ChatMessage(BaseModel):
    _id: str
    senderId: int
    receiverId: int
    content: str
    timestamp: datetime


class MessageAuthor(BaseModel):
    senderId: int
    receiverId: int


class Friendship(BaseModel):
    user_id: int
    friend_id: int
    status: str
    initiated_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()



class BaseNotification(BaseModel):
    _id: Optional[str] = None
    user_id: int
    type: Literal["Game Invite", "Player/Game Report", "Friend Request"]
    content: dict
    timestamp: datetime = datetime.now()
    read: bool = False


class GameInvitePayload(BaseModel):
    game_id: int
    inviter_id: int
    inviter_name: str
    game_details: Optional[str] = None


class PlayerGameReportPayload(BaseModel):
    reported_id: int
    reporter_id: int
    report_reason: str
    game_id: Optional[int] = None
    additional_details: Optional[str] = None


class FriendRequestPayload(BaseModel):
    requester_id: int
    requester_name: str
    additional_message: Optional[str] = None
