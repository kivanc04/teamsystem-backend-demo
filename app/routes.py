from fastapi import APIRouter, HTTPException
from app.schemas import Item, ItemCreate
from app.repository import InMemoryItemRepo

router = APIRouter()
repo = InMemoryItemRepo()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    return repo.create(payload)


@router.get("/items", response_model=list[Item])
def list_items():
    return repo.list()


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = repo.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
