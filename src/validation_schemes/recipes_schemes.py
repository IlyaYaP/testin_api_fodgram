from typing import Optional, Union

from pydantic import (AnyUrl, BaseModel, EmailStr, Field, HttpUrl, constr,
                      validator)

from src.errors import ErrorMessaages
from .user_schemes import Users
from .tags_schemes import Tags
from .ingredients_schemes import Ingredients


class RecipesResult(BaseModel):
    id: int
    tags: list[Tags]
    author: Users = Field(...)
    ingredients: list[Ingredients]
    is_favorited: bool = Field(...)
    is_in_shopping_cart: bool = Field(...)
    name: constr(max_length=150) = Field(...)
    image: AnyUrl
    text: str = Field(...)
    cooking_time: int = Field(...)


class Recipes(BaseModel):
    count: int
    next: Union[str, None]
    previous: Union[str, None]
    results: list[RecipesResult]


class RecipesValidationError(BaseModel):
    cooking_time: list = Field(...)

    @validator("cooking_time")
    def validate_cooking_time(cls, value):
        if value[0] not in ErrorMessaages.WRONG_VALIDATE_ERRORS:
            raise ValueError(f'Что то пошло не так, {value[0]}')
        

class RecipesNotLoggedError(BaseModel):
    detail: str = Field(...)