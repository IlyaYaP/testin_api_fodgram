from typing import Optional, Union

from pydantic import (AnyUrl, BaseModel, EmailStr, Field, HttpUrl, constr,
                      validator)

from src.errors import ErrorMessaages
from .user_schemes import Users
from .tags_schemes import Tags
from .ingredients_schemes import Ingredients

class ShoppingCart(BaseModel):
    id: int
    name: constr(max_length=150) = Field(...)
    image: AnyUrl
    cooking_time: int = Field(...)

class ShoppingCartError(BaseModel):
    errors: list[str]