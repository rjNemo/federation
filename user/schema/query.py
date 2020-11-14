from ariadne import QueryType

from user.models.user import User

query = QueryType()


@query.field("user")
def resolve_user(*_, name: str):
    return User(name=name)
