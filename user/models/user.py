from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field, validator


class User(BaseModel):
    id: str = Field(default_factory=uuid4)
    name: str = "John"

    @property
    def email(self) -> str:
        return f"{self.name.lower().replace(' ', '_')}@mail.com"


FORBIDDEN_NAMES = ["joe dalton"]


class UserInput(BaseModel):
    name: str

    class Config:
        anystr_strip_whitespace = True

    @validator("name")
    def name_must_contain_space(cls, name: str) -> str:
        if " " not in name:
            raise ValueError("must contain a space")
        return name.title()

    @validator("name")
    def name_must_not_be(cls, name: str) -> str:
        if name in FORBIDDEN_NAMES:
            raise ValueError("This name is forbidden")
        return name


class UserResponse(BaseModel):
    success: bool = True
    errorMessage: Optional[str] = None
    user: Optional[User] = None
