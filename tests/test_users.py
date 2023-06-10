import requests
import pytest
import allure

from src.base_validate import Response
from src.data import UsersData
from src.endpoints import UsersEndPoints
from src.api_objects.users_object import UsersValidate
from src.validation_schemes import InvalidUserRegistration, UserList


@pytest.mark.test_user_list
@allure.story('Тест получения списка пользователей.')
def test_users_list():
    r = requests.get(url=UsersEndPoints.LIST_USERS)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(UserList)


@pytest.mark.test_user_registration
@allure.story('Тест регистрации пользователя.')
def test_user_registration():
    r = requests.post(url=UsersEndPoints.USER_REGISTRATION,
                      data=UsersData.USER_REGISTRATION_DATA)
    response = UsersValidate(r)
    response.user_validate()


@pytest.mark.test_negative_user_registration
@allure.story('Негативный тест регистрации пользователя: указываем невалидные данные.')
def test_negative_user_registration():
    r = requests.post(url=UsersEndPoints.USER_REGISTRATION,
                      data=UsersData.INVALID_USER_REGISTRATION_DATA)
    response = Response(r)
    response.assert_status_code(400)
    response.validate(InvalidUserRegistration)
