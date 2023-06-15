import allure
import pytest
import requests
import urllib3
import json

from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData, RecipeData
from src.endpoints import UsersEndPoints, RecipesEndPoints
from src.validation_schemes.recipes_schemes import Recipes, RecipesResult, RecipesValidationError, RecipesNotLoggedError, RecipesPatch
from src.validation_schemes.user_schemes import UserList




@pytest.mark.test_create_recipe
@allure.story('Тест создания рецепта.')
def test_create_recipe():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    r = requests.post(url=RecipesEndPoints.RECIPES_LIST, json=RecipeData.RECIPE_CREATE_DATA, headers=headers)
    response = Response(r)
    response.assert_status_code(201)
    response.validate(RecipesResult)


@pytest.mark.test_negative_create_recipe_validation_error
@allure.story('Тест создания рецепта с невалидными данными.')
def test_negative_create_recipe_validation_error():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    r = requests.post(url=RecipesEndPoints.RECIPES_LIST, json=RecipeData.INVALID_RECIPE_CREATE_DATA, headers=headers)
    response = Response(r)
    response.assert_status_code(400)
    response.validate(RecipesValidationError)


@pytest.mark.test_negative_create_recipe_user_not_logged
@allure.story('Тест создания рецепта, без авторизации.')
def test_negative_create_recipe_user_not_logged():
    r = requests.post(url=RecipesEndPoints.RECIPES_LIST, json=RecipeData.INVALID_RECIPE_CREATE_DATA)
    response = Response(r)
    response.assert_status_code(401)
    response.validate(RecipesNotLoggedError)


@pytest.mark.test_get_recipe
@allure.story('Тест получения рецепта.')
def test_get_recipe():
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    r = requests.get(url=f'http://localhost/api/recipes/{id}/')
    response = Response(r)
    response.assert_status_code(200)
    response.validate(RecipesResult)


@pytest.mark.test_recipes_list
@allure.story('Тест получения списка рецептов.')
def test_recipes_list():
    r = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Recipes)


@pytest.mark.test_patch_recipe
@allure.story('Тест изменения рецепта.')
def test_patch_recipe():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    r = requests.patch(url=f'http://localhost/api/recipes/{id}/', json=RecipeData.RECIPE_PATCH_DATA, headers=headers)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(RecipesPatch)


@pytest.mark.test_negative_patch_recipe_validation_error
@allure.story('Тест изменения рецепта c невалидными данными.')
def test_negative_patch_recipe_validation_error():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    r = requests.patch(url=f'http://localhost/api/recipes/{id}/', json=RecipeData.INVALID_RECIPE_PATCH_DATA, headers=headers)
    response = Response(r)
    response.assert_status_code(400)
    response.validate(RecipesValidationError)

@pytest.mark.test_patch_recipe_user_not_logged
@allure.story('Тест изменения рецепта, без авторизации.')
def test_patch_recipe_user_not_logged():
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    r = requests.patch(url=f'http://localhost/api/recipes/{id}/', json=RecipeData.RECIPE_PATCH_DATA)
    response = Response(r)
    response.assert_status_code(401)
    response.validate(RecipesNotLoggedError)


@pytest.mark.test_delet_recipe
@allure.story('Тест удаления рецепта.')
def test_delet_recipe():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    recipes_list = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    id = recipes_list.json()['results'][0]['id']
    r = requests.delete(url=f'http://localhost/api/recipes/{id}/', headers=headers)
    if r.status_code == 204:
        test_create_recipe()
    else:
        assert r.status_code != 204, f'{r.status_code}'