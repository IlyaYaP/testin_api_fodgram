from typing import Optional, Union

from pydantic import (AnyUrl, BaseModel, EmailStr, Field, HttpUrl, constr, conint,
                      validator)
from pydantic.color import Color
from src.errors import ErrorMessaages


class Tags(BaseModel):
    id: int
    name: constr(max_length=200)
    color: Color
    slug: constr(max_length=200) = Field(regex='^[-a-zA-Z0-9_]+$')

class TagsError(BaseModel):
    detail: str
