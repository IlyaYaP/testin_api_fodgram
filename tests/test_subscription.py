import allure
import pytest
import requests

from src.api_objects.subscribe_object import SubscribeValidate
from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData
from src.endpoints import SubscriptionEndPoints, UsersEndPoints
from src.validation_schemes.errors_schemes import Error401
from src.validation_schemes.subscribe_schemes import Subscribe, Subscriptions


@pytest.mark.test_subscribe_to_user
@allure.story('Тест подписки на пользователя.')
def test_subscribe_to_user():
    headers = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_subscription = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.post(url=url_subscription, headers=headers)
    response = Response(r)
    response.assert_status_code(201)
    response.validate(Subscribe)


@pytest.mark.test_negative_subscribe_to_user_not_logged
@allure.story('Тест подписки на пользователя, без авторизации.')
def test_negative_subscribe_to_user_not_logged():
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_subscription = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.post(url=url_subscription)
    response = SubscribeValidate(r)
    response.assert_status_code(401)
    response.validate(Error401)


@pytest.mark.test_get_subscriptions
@allure.story('Тест получения подписок пользователя пользователя.')
def test_get_subscriptions():
    headers = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    r = requests.get(url=SubscriptionEndPoints.MY_SUBSCRIPTION, headers=headers)
    response = SubscribeValidate(r)
    response.assert_status_code(200)
    response.validate(Subscriptions)


@pytest.mark.test_get_subscriptions_user_not_logged
@allure.story('Тест получения подписок пользователя пользователя без авторизации.')
def test_get_subscriptions_user_not_logged():
    r = requests.get(url=SubscriptionEndPoints.MY_SUBSCRIPTION)
    response = SubscribeValidate(r)
    response.assert_status_code(401)
    response.validate(Error401)


@pytest.mark.test_unsubscribe_to_user
@allure.story('Тест отписки от пользователя.')
def test_unsubscribe_to_user():
    headers = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_subscription = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.delete(url=url_subscription, headers=headers)
    response = NoResponse(r)
    response.assert_status_code(204)


@pytest.mark.test_unsubscribe_error
@allure.story('Тест отписки от пользователя.')
def test_unsubscribe_error():
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_subscription = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.delete(url=url_subscription)
    response = Response(r)
    response.assert_status_code(401)
