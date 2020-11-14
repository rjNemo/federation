from pydantic.dataclasses import dataclass


@dataclass
class Product:
    upc: str
    name: str
    price: int
    weight: int
