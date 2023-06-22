import allure
import pytest
import requests

from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData
from src.endpoints import UsersEndPoints, RecipesEndPoints, IngredientsEndPoints
from src.validation_schemes.ingredients_schemes import Ingredients

@pytest.mark.test_ingredients_list
@allure.story('Тест получения списка рецептов.')
def test_ingredients_list():
    r = requests.get(url=IngredientsEndPoints.INGREDIENTS_LIST)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Ingredients)

@pytest.mark.test_get_ingredient
@allure.story('Тест получения определенного ингредиента.')
def test_get_ingredient():
    r = requests.get(url='http://localhost/api/ingredients/123/')
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Ingredients)