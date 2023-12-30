from typing import List

from project import product
from project.product import Product
# from project.drink import Drink
# from project.food import Food


class ProductRepository:
    def __init__(self):
        self.products: List[product: Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str or None:
        ret = [p for p in self.products if p.name == product_name]
        if ret:
            return ret[0]

    def remove(self, product_name: str) -> None:
        ret = self.find(product_name)
        if ret is not None:
            self.products.remove(ret)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
