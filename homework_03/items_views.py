from fastapi import APIRouter

router = APIRouter(tags=["Items"])


@router.get("/")
async def items_list():
    return {"items": [{"id": 1, "name": "item-01"}, {"id": 2, "name": "test"}]}


@router.post("/")
async def create_item(data: dict):
    return {"data": data}


@router.get("/{item_id}/")
async def get_item(item_id: int):
    return {"data": {"id": item_id / 2, "name": f"item-{item_id}"}}
