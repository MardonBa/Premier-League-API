from fastapi import APIRouter

router = APIRouter(
    prefix="/players",
    tags=["players"],
)

@router.get("/{name}")
async def get_player_by_name(name: str):
    pass

@router.get("/{name}/club")
async def get_player_club(name: str):
    pass

@router.get("/{name}/position")
async def get_player_position(name: str):
    pass

@router.get("/{player}/nationality")
async def get_player_nationality(player: str):
    pass

@router.get("/{name}/age")
async def get_player_age(name: str):
    pass

@router.get("/{name}/stats/{stat_type}")
async def get_player_stats(name: str, stat_type: str):
    pass


@router.get("/{name}/stats/{stat_type}/{state_name}")
async def get_player_sub_stats(name: str, stat_type: str, state_name: str):
    pass

@router.get("/{name}/fpl_price")
async def get_player_fpl_price(name: str):
    pass

@router.get("/{name}/fpl_points")
async def get_player_fpl_points(name: str):
    pass

@router.get("/{name}/fpl_points_by_week")
async def get_player_fpl_points_by_week(name: str):
    pass