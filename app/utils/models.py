from pydantic import BaseModel
from datetime import datetime

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
