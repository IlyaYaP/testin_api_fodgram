import allure
import pytest
import requests
import urllib3
import json
from pathlib import Path

from src.api_objects.users_object import UsersValidate
from src.api_objects.subscribe_object import SubscribeValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData, RecipeData
from src.endpoints import UsersEndPoints, RecipesEndPoints, ShoppingCartEndPoints, SubscriptionEndPoints
from src.validation_schemes.recipes_schemes import Recipes, RecipesResult
from src.validation_schemes.user_schemes import UserList, UsersProfileError
from src.validation_schemes.shopping_cart_schemes import ShoppingCart
from src.validation_schemes.subscribe_schemes import SubscribeError_401

@pytest.mark.test_subscribe_to_user
@allure.story('Тест подписки на пользователя.')
def test_subscribe_to_user():
    headers = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_shopping_cart = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.post(url=url_shopping_cart, headers=headers)
    response = SubscribeValidate(r)
    response.subscribe_validate()


@pytest.mark.test_negative_subscribe_to_user_not_logged
@allure.story('Тест подписки на пользователя, без авторизации.')
def test_negative_subscribe_to_user_not_logged():
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_shopping_cart = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.post(url=url_shopping_cart)
    response = SubscribeValidate(r)
    response.assert_status_code(401)
    response.validate(SubscribeError_401)















@pytest.mark.test_unsubscribe_to_user
@allure.story('Тест отписки от пользователя.')
def test_unsubscribe_to_user():
    headers = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    user_id = UsersValidate.user_id(url=UsersEndPoints.LIST_USERS)
    url_shopping_cart = f'http://localhost/api/users/{user_id}/subscribe/'
    r = requests.delete(url=url_shopping_cart, headers=headers)
    # response = SubscribeValidate(r)
    # response.subscribe_validate()


