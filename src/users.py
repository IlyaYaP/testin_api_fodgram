from src.base_validate import Response
from src.validation_schemes import InvalidUserRegistration, UserRegistration


class UsersValidate(Response):

    def user_validate(self):
        if self.response_status == 200:
            UserRegistration.parse_obj(self.response_json)
            print(f'status_code = {self.response_status}, respone = {self.response_json}')
        elif self.response_status == 400:
            InvalidUserRegistration.parse_obj(self.response_json)
            print(f'status_code = {self.response_status}, respone = {self.response_json}')
        else:
            assert self.response_status != 400 or 200, 'Что то пошло не так.'
