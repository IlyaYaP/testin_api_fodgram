import allure
import pytest
import requests
import urllib3
import json
from pathlib import Path

from src.api_objects.recipe_object import RecipeValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData, RecipeData
from src.endpoints import UsersEndPoints, RecipesEndPoints, ShoppingCartEndPoints
from src.validation_schemes.recipes_schemes import Recipes, RecipesResult
from src.validation_schemes.user_schemes import UserList, UsersProfileError
from src.validation_schemes.shopping_cart_schemes import ShoppingCart

@pytest.mark.test_add_recipe_favorites
@allure.story('Тест добавления рецептов в избранное')
def test_add_recipe_favorites():
    headers = Response.user_auth_token(data=UsersData.LOGIN_USER_TOKEN_DATA)
    recipe_id = RecipeValidate.recipe_id(url=RecipesEndPoints.RECIPES_LIST)
    url_shopping_cart = f'http://localhost/api/recipes/{recipe_id}/favorite/'
    r = requests.post(url=url_shopping_cart, headers=headers)
    print(r.status_code)