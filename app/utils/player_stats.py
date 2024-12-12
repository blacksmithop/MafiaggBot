from app.utils.models import PlayerStats
from mafiagg.user import GetUser


player = GetUser(cookie=None)  # We dont need auth to fetch players

# TODO: Implement search by name


def get_player_data(id: int = None, username: str = None, report=False):
    if id:
        player = GetUser().get_user(id=id)
        return player
    if username:
        player = GetUser().get_user(id=533610)  # TODO: Look up DB for game reports
        if report:
            player = PlayerStats(
                id=player.id, username=player.username, createdAt=player.createdAt
            )
            return player
        # TODO: If not exact match, get all similar player names
        return [player]
