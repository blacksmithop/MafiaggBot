from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime

class Login(BaseModel):
    username: str
    password: str

class PlayerStats(BaseModel):
    id: int
    username: str
    createdAt: str
    totalGames: int = 1
    winRate: int = 0
    townWinRate: int = 0
    mafiaWinRate: int = 0
    neutralWinRate: int = 0

class ChatMessage(BaseModel):
    id: str
    sender: str
    content: str
    timestamp: datetime
    type: str = Literal["text", "image"]