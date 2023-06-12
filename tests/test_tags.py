import allure
import pytest
import requests

from src.api_objects.users_object import UsersValidate
from src.base_validate import NoResponse, Response
from src.data import UsersData
from src.endpoints import UsersEndPoints, TagsEndPoints
from src.validation_schemes.user_schemes import (InvalidChangingPassword,
                                                 InvalidUserRegistration,
                                                 UserList,
                                                 Users, UsersProfileError)
from src.validation_schemes.tags_schemes import (Tags, TagsError)

@pytest.mark.test_tags_list
@allure.story('Тест получения списка тегов.')
def test_tags_list():
    r = requests.get(url=TagsEndPoints.LIST_TAGS)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Tags)


@pytest.mark.test_negative_not_found
@allure.story('Тест получения несуществующего тега.')
def test_negative_tags_not_found():
    r = requests.get(url=TagsEndPoints.TAGS_NOT_FOUND)
    response = Response(r)
    response.assert_status_code(404)
    response.validate(TagsError)