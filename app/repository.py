from typing import Dict, List, Optional
from app.schemas import Item, ItemCreate


class InMemoryItemRepo:
    def __init__(self) -> None:
        self._items: Dict[int, Item] = {}
        self._next_id: int = 1

    def list(self) -> List[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Optional[Item]:
        return self._items.get(item_id)

    def create(self, data: ItemCreate) -> Item:
        item = Item(id=self._next_id, name=data.name, price=data.price)
        self._items[self._next_id] = item
        self._next_id += 1
        return item
