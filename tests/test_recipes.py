import allure
import pytest
import requests

from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData, RecipeData
from src.endpoints import UsersEndPoints, RecipesEndPoints
from src.validation_schemes.recipes_schemes import Recipes, RecipesResult, RecipesValidationError, RecipesNotLoggedError
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
    print(r.json())
    response.validate(RecipesNotLoggedError)






@pytest.mark.test_recipes_list
@allure.story('Тест получения списка рецептов.')
def test_recipes_list():
    r = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Recipes)
