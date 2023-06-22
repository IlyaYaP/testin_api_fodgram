from typing import Optional, Union

from pydantic import (AnyUrl, BaseModel, EmailStr, Field, HttpUrl, constr,
                      validator)

from src.errors import ErrorMessaages
from .user_schemes import Users
from .tags_schemes import Tags


# "id": 0,
# "name": "Картофель отварной",
# "measurement_unit": "г",
# "amount": 1
class Ingredients(BaseModel):
    id: int
    name: constr(max_length=200) = Field(...)
    measurement_unit: constr(max_length=200) = Field(...)