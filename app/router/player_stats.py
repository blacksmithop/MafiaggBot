from fastapi import APIRouter, Request
from app.utils.player_stats import get_player_data, PlayerStats
from typing import List, Union
from mafiagg.models.models import SearchUser
from app.utils.player_stats import PlayerStats

router = APIRouter()


@router.get("/players/get_player_by_id/{player_id}")
async def get_player_by_id(request: Request, player_id: int) -> SearchUser:
    player = get_player_data(id=player_id)
    return player


@router.get("/players/get_player_by_name/{username}")
async def get_player_by_name(request: Request, username: str) -> Union[List[SearchUser], List]:
    try:
        matched_players = get_player_data(username=username)
    except Exception:
        matched_players = []
    return matched_players


@router.get("/players/get_player_report/{username}")
async def get_player_by_name(request: Request, username: str) -> PlayerStats:
    player = get_player_data(username=username, report=True)
    return player
