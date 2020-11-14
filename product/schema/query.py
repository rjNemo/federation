from random import choice, randint
from string import ascii_letters

from ariadne import QueryType

from product.models.product import Product

query = QueryType()


@query.field("topProducts")
def resolve_top_products(*_, first: int):
    return [
        Product(
            upc=choice(ascii_letters),
            price=randint(0, first),
            weight=randint(0, first),
            name=choice(ascii_letters),
        )
    ] * first
