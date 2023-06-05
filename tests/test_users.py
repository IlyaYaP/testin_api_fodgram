import requests
from src.endpoints import UsersEndPoints
from src.baseclasse import Response


def test_users():
    r = requests.get(url=UsersEndPoints.LIST_USERS)
    response = Response(r)
    response.assert_status_code(200)
    # response.validate()
