from pydantic import BaseModel
from mafiagg.user import GetUser


player = GetUser()

class PlayerStats(BaseModel):
    id: int
    username: str
    createdAt: str
    totalGames: int = 1
    winRate: int = 0
    townWinRate: int = 0
    mafiaWinRate: int = 0
    neutralWinRate: int = 0

# TODO: Implement search by name
# First we need to index all players

def get_player_data(id: int=None, username: str= None, report=False):
    if id:
        player = GetUser().get_user(id=id)
        # player = PlayerStats(id=data.id, username=data.username, createdAt=data.createdAt)
        return player
    if username:
        player = GetUser().get_user(id=533610) # TODO: Look up DB for game reports
        if report:
            player = PlayerStats(id=player.id, username=player.username, createdAt=player.createdAt)
            return player
        # TODO: If not exact match, get all similar player names
        return [player]
