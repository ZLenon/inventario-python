from inventory_report.product import Product
from typing import List, Optional


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        self._infos = data or list()

    def add_data(self, data: List[Product]) -> None:
        self._infos.extend(data)

    @property
    def data(self) -> List[Product]:
        return self._infos
