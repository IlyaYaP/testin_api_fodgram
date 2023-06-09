import requests

from src.base_validate import Response
from src.endpoints import UsersEndPoints
from src.validation_schemes import UserList, UserRegistration, InvalidUserRegistration
from src.data import UsersData
from src.users import UsersValidate


def test_users_list():
    r = requests.get(url=UsersEndPoints.LIST_USERS)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(UserList)


def test_user_registration():
    r = requests.post(url=UsersEndPoints.USER_REGISTRATION, data=UsersData.USER_REGISTRATION_DATA)
    response = UsersValidate(r)
    response.user_bad_request()
    # требуется обработать статус 400, когда пользователь с такими данными уже есть
    response.user_validate()


def test_negative_user_registration():
    r = requests.post(url=UsersEndPoints.USER_REGISTRATION, data=UsersData.INVALID_USER_REGISTRATION_DATA)
    response = Response(r)
    response.assert_status_code(400)
    response.validate(InvalidUserRegistration)
    print(r.status_code)
    print(r.json())

