from typing import Union, Optional

from pydantic import AnyUrl, BaseModel, EmailStr, HttpUrl, constr, validator, Field
from src.errors import ErrorMessaages


class Users(BaseModel):
    id: int
    email: EmailStr
    username: constr(max_length=150) = Field(...)
    first_name: constr(max_length=150)
    last_name: constr(max_length=150)
    is_subscribed: bool


class UserList(BaseModel):
    count: int
    next: Union[str, None]
    previous: Union[str, None]
    results: list[Users]


class UserRegistration(BaseModel):
    id: int
    email:  EmailStr
    username: constr(max_length=150) = Field(...)
    first_name: constr(max_length=150)
    last_name: constr(max_length=150)


class InvalidUserRegistration(BaseModel):
    id: Union[int, None]
    email: list = Field(...)
    username: list = Field(...)
    first_name: Union[list, None]
    last_name: Union[list, None]
    password: Union[list, None]

    @validator("email", "username")
    def validatet_email(cls, value):
        if value[0] not in ErrorMessaages.WRONG_VALIDATE_ERRORS:
            raise ValueError(f'Что то пошло не так, {value[0]}')

        # for error in ErrorMessaages.WRONG_VALIDATE_ERRORS:
        #     if value != error:
        #         raise ValueError(f'Что то пошло не так, {value}, {error}')

