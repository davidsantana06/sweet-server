from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declared_attr

from .model import Model


class Resource(Model):
    @declared_attr
    def name(cls):
        return Column(String(100), nullable=False)

    @declared_attr
    def brand(cls):
        return Column(String(100))

    @declared_attr
    def supplier(cls):
        return Column(String(100))

    @declared_attr
    def value(cls):
        return Column(Float(), nullable=False)

    @declared_attr
    def current_quantity(cls):
        return Column(Float(), nullable=False)

    @declared_attr
    def minimum_quantity(cls):
        return Column(Integer(), nullable=False)

    def __init__(
        self,
        name: str, brand: str, supplier: str, value: float,
        current_quantity: float, minimum_quantity: int
    ) -> None:
        self.name = name
        self.brand = brand
        self.supplier = supplier
        self.value = value
        self.current_quantity = current_quantity
        self.minimum_quantity = minimum_quantity
