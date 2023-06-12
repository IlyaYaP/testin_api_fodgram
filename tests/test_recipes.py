import allure
import pytest
import requests

from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData
from src.endpoints import UsersEndPoints, RecipesEndPoints
from src.validation_schemes.user_schemes import (InvalidChangingPassword,
                                                 InvalidUserRegistration,
                                                 UserList,
                                                 Users, UsersProfileError)



@pytest.mark.test_create_recipe
@allure.story('Тест создания рецепта.')
def test_create_recipe():
    token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    headers = {'Authorization': f'Token {token}'}
    r = requests.post(url=RecipesEndPoints.RECIPES_LIST, headers=headers, data=UsersData.RECIPE_CREATE_DATA)
    response = Response(r)
    response.assert_status_code(200)
    print(r.json())
    # response.validate(UserList)

@pytest.mark.test_recipes_list
@allure.story('Тест получения списка рецептов.')
def test_recipes_list():
    r = requests.get(url=RecipesEndPoints.RECIPES_LIST)
    response = Response(r)
    response.assert_status_code(200)
    print(r.json())
    # response.validate(UserList)