from pydantic.dataclasses import dataclass

from product.models.product import Product
from user.models.user import User


@dataclass
class Review:
    id: int
    body: str
    author: User
    product: Product
