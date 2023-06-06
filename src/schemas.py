from typing import Union

from pydantic import AnyUrl, BaseModel, EmailStr, HttpUrl, constr, validator


class Users(BaseModel):
    id: int
    email: EmailStr
    username: constr(max_length=150)
    first_name: constr(max_length=150)
    last_name: constr(max_length=150)
    is_subscribed: bool


class UserList(BaseModel):
    count: int
    next: Union[str, None]
    previous: Union[str, None]
    results: list[Users]








# input_json = {'count': 3, 'next': None, 'previous': None, 'results': [
#         {'id': 1, 'email': 'admin@mail.ru', 'username': 'admin', 'first_name': 'admin', 'last_name': 'admin', 'is_subscribed': False
#         },
#         {'id': 14, 'email': 'vasily@yandex.ru', 'username': 'Vasily_Ivanov', 'first_name': 'Vasily', 'last_name': 'Ivanov', 'is_subscribed': False
#         },
#         {'id': 15, 'email': 'ivan@yandex.ru', 'username': 'Ivan_A', 'first_name': 'Ivan', 'last_name': 'Aleksandrivich', 'is_subscribed': False
#         }
#     ]
# }
