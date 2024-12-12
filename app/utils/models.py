from pydantic import BaseModel

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
