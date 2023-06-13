import allure
import pytest
import requests

from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData
from src.endpoints import UsersEndPoints, RecipesEndPoints, IngredientsEndPoints
from src.validation_schemes.user_schemes import (InvalidChangingPassword,
                                                 InvalidUserRegistration,
                                                 UserList,
                                                 Users, UsersProfileError)


@pytest.mark.test_ingredients_list
@allure.story('Тест получения списка рецептов.')
def test_ingredients_list():
    # token = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    # headers = {'Authorization': f'Token {token}'}
    r = requests.get(url=IngredientsEndPoints.INGREDIENTS_LIST)
    # response = Response(r)
    # response.assert_status_code(200)
    print(r.json())
    print(r.status_code)
    # response.validate(UserList)