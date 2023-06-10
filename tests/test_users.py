import requests
import pytest
import allure

from src.base_validate import Response
from src.data import UsersData
from src.endpoints import UsersEndPoints
from src.api_objects.users_object import UsersValidate
from src.validation_schemes import InvalidUserRegistration, UserList, Users


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


@pytest.mark.test_get_user_profile
@allure.story('Тест получения информации о пользователе.')
def test_get_user_profile():
    r = requests.post(url=UsersEndPoints.USER_TOKEN, data=UsersData.LOGIN_USER_TOKEN_DATA)
    response = UsersValidate(r)
    token = response.user_auth_token()
    headers = {'Authorization': f'Token {token}'}
    r = requests.get(url=UsersEndPoints.USER_PROFILE, headers=headers)
    response = UsersValidate(r)
    response.assert_status_code(200)
    response.validate(Users)


@pytest.mark.test_nagative_get_user_profile
@allure.story('Тест получения информации о пользователе.')
def test_negative_get_user_profile():
    r = requests.post(url=UsersEndPoints.USER_TOKEN, data=UsersData.LOGIN_USER_TOKEN_DATA)
    response = UsersValidate(r)
    token = response.user_auth_token()
    headers = {'Authorization': f'Token {token}'}
    r = requests.get(url=UsersEndPoints.INVALIDE_USER_PROFILE, headers=headers)
    response = UsersValidate(r)
    response.assert_status_code(404)
    # написать валидатор для 404
    # response.validate(Users)

@pytest.mark.test_nagative_get_user_profile_401
@allure.story('Тест получения информации о пользователе.')
def test_negative_get_user_profile_401():
    r = requests.get(url=UsersEndPoints.USER_PROFILE)
    response = UsersValidate(r)
    response.assert_status_code(401)
    # написать валидатор для 401
    # response.validate(Users)