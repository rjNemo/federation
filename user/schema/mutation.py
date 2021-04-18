from ariadne import MutationType, convert_kwargs_to_snake_case

from user.models.user import User, UserResponse, UserInput

mutation = MutationType()


def create_user(user_input: UserInput) -> User:
    """Create a user

    :param user_input: validated user input object
    :return: user newly created
    """
    return User(name=user_input.name)


@mutation.field("createUser")
@convert_kwargs_to_snake_case
def resolve_create_user(*_, user_data: dict) -> UserResponse:
    try:
        user_input = UserInput(name=user_data["name"])
        user = create_user(user_input)
        return UserResponse(user=user)
    except ValueError as error:
        return UserResponse(success=False, errorMessage=str(error))
