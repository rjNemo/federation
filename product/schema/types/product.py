from ariadne.contrib.federation import FederatedObjectType

from product.models.product import Product

product = FederatedObjectType("Product")


@product.reference_resolver
def resolve_product_reference(*_, representation):
    print(representation)
    return Product(upc="id", name="product", price=10, weight=12)
