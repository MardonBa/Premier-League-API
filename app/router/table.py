from fastapi import APIRouter

router = APIRouter(
    prefix="/table",
    tags=["table"],
)

@router.get("/")
async def get_league_table():
    return {"message": "League table data"}