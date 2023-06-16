import allure
import pytest
import requests
import urllib3
import json
from pathlib import Path

from src.api_objects.shopping_cart_object import ShoppingCartValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData, RecipeData
from src.endpoints import UsersEndPoints, RecipesEndPoints, ShoppingCartEndPoints
from src.validation_schemes.recipes_schemes import Recipes, RecipesResult
from src.validation_schemes.user_schemes import UserList, UsersProfileError
from src.validation_schemes.shopping_cart_schemes import ShoppingCart


@pytest.mark.test_add_shopping_cart
@allure.story('Тест добавления рецептов в список покупок.')
def test_add_shopping_cart():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    url_shopping_cart = f'http://localhost/api/recipes/{id}/shopping_cart/'
    r = requests.post(url=url_shopping_cart, headers=headers)
    response = ShoppingCartValidate(r)
    response.shopping_cart_validate()


@pytest.mark.test_download_shopping_cart
@allure.story('Тест скачивания списка покупок.')
def test_download_shopping_cart():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    r = requests.get(url=ShoppingCartEndPoints.DOWNLOAD_SHOPPING_CART, headers=headers)

    with allure.step('Скачем списко покупок и проверим, что он появился в корне проекта.'):
        if r.status_code == 200:
            filename = Path('shopping_cart.pdf')
            filename.write_bytes(r.content)
        else:
            assert f'Статус код = {r.status_code}'


@pytest.mark.test_negative_download_shopping_cart_not_logged
@allure.story('Тест скачивания списка покупок, без авторизации')
def test_negative_download_shopping_cart_not_logged():
    r = requests.get(url=ShoppingCartEndPoints.DOWNLOAD_SHOPPING_CART)
    print(r.json())
    response = Response(r)
    response.assert_status_code(401)
    response.validate(UsersProfileError)


@pytest.mark.test_delete_shopping_cart
@allure.story('Тест удаления рецептов из списка покупок.')
def test_delete_shopping_cart():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    url_shopping_cart = f'http://localhost/api/recipes/{id}/shopping_cart/'
    r = requests.delete(url=url_shopping_cart, headers=headers)
    response = NoResponse(r)
    response.assert_status_code(204)


@pytest.mark.test_negative_delete_shopping_cart_not_logged
@allure.story('Тест скачивания списка покупок, без авторизации')
def test_negative_delete_shopping_cart_not_logged():
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    url_shopping_cart = f'http://localhost/api/recipes/{id}/shopping_cart/'
    r = requests.delete(url=url_shopping_cart)
    response = NoResponse(r)
    response.assert_status_code(401)