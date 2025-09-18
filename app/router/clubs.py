from fastapi import APIRouter

router = APIRouter(
    prefix="/clubs",
    tags=["clubs"],
)

@router.get("/{name}/table_info")
async def get_club_table_info(name: str):
    pass

@router.get("/{name}/players")
async def get_club_players(name: str):
    pass

@router.get("/{name}/players/{position}")
async def get_club_players_by_position(name: str, position: str):
    pass

@router.get("/{name}/{stat_type}")
async def get_club_stats(name: str, stat_type: str):
    pass

@router.get("/{name}/{stat_type}/{state_name}")
async def get_club_sub_stats(name: str, stat_type: str, state_name: str):
    pass