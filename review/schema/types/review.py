from random import choice
from string import ascii_letters

from ariadne.contrib.federation import FederatedObjectType

from review.models.review import Review

review = FederatedObjectType("Review")


@review.reference_resolver
def resolve_reviews_reference(_, _info, representation):
    print(representation)
    return Review(id=representation["id"], body=choice(ascii_letters))
