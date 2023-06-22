from typing import Optional, Union

from pydantic import (AnyUrl, BaseModel, EmailStr, Field, HttpUrl, constr,
                      validator)



class RecipesResult(BaseModel):
    id: int
    name: constr(max_length=150) = Field(...)
    image: AnyUrl
    cooking_time: int = Field(...)

class SubscribeError_401(BaseModel):
    detail: str = Field(...)


class SubscribeErrors(BaseModel):
    errors: list[str]

class Subscribe(BaseModel):
    id: int
    email: EmailStr
    username: constr(max_length=150) = Field(...)
    first_name: constr(max_length=150)
    last_name: constr(max_length=150)
    is_subscribed: bool
    recipes: list[RecipesResult]
    recipes_count: int
