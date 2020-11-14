from random import choice, randint
from string import ascii_letters

from ariadne import QueryType

from product.models.product import Product
from review.models.review import Review
from user.models.user import User

query = QueryType()


@query.field("reviews")
def resolve_reviews(*_, first: int):
    return [
        Review(
            id=randint(0, first),
            body=choice(ascii_letters),
            author=User(),
            product=Product(upc="id", name="product", price=10, weight=12),
        )
    ] * first
