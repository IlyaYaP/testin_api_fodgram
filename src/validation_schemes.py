from typing import Union

from pydantic import AnyUrl, BaseModel, EmailStr, HttpUrl, constr, validator, Field


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
    email: EmailStr
    username: constr(max_length=150) = Field(...)
    first_name: constr(max_length=150)
    last_name: constr(max_length=150)
