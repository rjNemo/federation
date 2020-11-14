from ariadne import MutationType

from user.models.user import User, UserResponse, UserInput

mutation = MutationType()


def create_user(user_input: UserInput) -> User:
    """Create a user

    :param user_input: validated user input object
    :return: user newly created
    """
    return User(name=user_input.name)


@mutation.field("createUser")
def resolve_create_user(*_, input: dict) -> UserResponse:
    try:
        user_input = UserInput(name=input.get("name"))
        user = create_user(user_input)
        return UserResponse(user=user)
    except ValueError as error:
        return UserResponse(success=False, errorMessage=str(error))
