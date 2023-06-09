from src.base_validate import Response
from src.validation_schemes import UserList, UserRegistration, InvalidUserRegistration


class UsersValidate(Response):

    def user_bad_request(self):
        if self.response_status == 200:
            
            print(f'status_code = {self.response_status}, respone = {self.response_json}')
        elif self.response_status == 400:
            print(f'status_code = {self.response_status}, respone = {self.response_json}')
        else:
            assert self.response_status != 400 or 200, 'Что то пошло не так.'

    def user_validate(self):
        if self.response_status == 200:
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    UserRegistration.parse_obj(item)
        else:
            InvalidUserRegistration.parse_obj(self.response_json)

