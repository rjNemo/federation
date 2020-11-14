from pydantic.dataclasses import dataclass

from product.models.product import Product
from user.models.user import User


@dataclass
class Review:
    id: str
    body: str
    author: User
    product: Product
