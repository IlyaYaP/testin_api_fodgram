import requests

from src.baseclasse import Response_response
from src.endpoints import UsersEndPoints
from src.schemas import UserList


def test_users():
    r = requests.get(url=UsersEndPoints.LIST_USERS)
    response = Response_response(r)
    response.assert_status_code(200)
    response.validate(UserList)
    print(r.json())
