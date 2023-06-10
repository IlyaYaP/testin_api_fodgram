import allure
import requests
from src.base_validate import Response
from src.validation_schemes import InvalidUserRegistration, UserRegistration
from src.data import UsersData
from src.endpoints import UsersEndPoints


class UsersValidate(Response):

    def user_validate(self):
        with allure.step('Проверяем статус-код и валидность ответа:'):
            if self.response_status == 200:
                with allure.step('Статус-код 200, пользователь успешно зарегистрирован, проверяем валидность ответа.'):
                    UserRegistration.parse_obj(self.response_json)
                    print(f'status_code = {self.response_status}, respone = {self.response_json}')
            elif self.response_status == 400:
                with allure.step('Статус-код 400, пользователь с такими данными уже существует, проверяем валидность ответа.'):
                    InvalidUserRegistration.parse_obj(self.response_json)
                    print(f'status_code = {self.response_status}, respone = {self.response_json}')
            else:
                assert self.response_status != 400 or 200, 'Что то пошло не так.'

    def user_auth_token(self):
        user_token = self.response_json["auth_token"]
        return user_token

