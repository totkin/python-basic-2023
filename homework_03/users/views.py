from fastapi import APIRouter

router = APIRouter(tags=["Users"])

@router.get("/")
async def get_users():
    pass

@router.post("/")
async def create_user():
    pass

@router.get("/{user_id}/")
async def get_user_by_id():
    pass

