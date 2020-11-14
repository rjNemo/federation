from ariadne.contrib.federation import FederatedObjectType

from user.models.user import User

user = FederatedObjectType("User")


@user.reference_resolver
def resolve_user_reference(_, _info, representation):
    print(representation)
    return User()
