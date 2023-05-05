"""Модуль содержит класс и методы с Api ручками"""
import allure

from .common import Common
from ..api_requests import Request


class ApiV1(Common):
    """Класс по работе с API"""

    def __init__(self):
        self.url = self.BASE_URL
        self.resourse_users = '/api/users/'
        self.resourse_unknown = '/api/unknown/'
        self.resourse_login = '/api/login/'
        self.resourse_register = '/api/register/'

    @allure.step('Шаг. Get запрос к API')
    def get_api_users(self, id_user: int):
        """Метод для отправки Get запроса, resourse - users

        Args:
            id_user: id пользователя

        Returns:
            Тело ответа
        """
        url = f'{self.url}{self.resourse_users}{id_user}'
        return Request().custom_request(method='GET', url=url)

    @allure.step('Шаг. Get запрос к API')
    def get_api_unknown(self, id_user: int):
        """Метод для отправки Get запроса, resourse - unknown

        Args:
            id_user: id пользователя

        Returns:
            Тело ответа
        """
        url = f'{self.url}{self.resourse_unknown}{id_user}'
        return Request().custom_request(method='GET', url=url)

    @allure.step('Шаг. Post запрос к API')
    def post_api_users(self, body_request: str):
        """Метод для отправки Post запроса, resourse - users

        Args:
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """

        url = f'{self.url}{self.resourse_users}'
        return Request().custom_request(method='POST', url=url, data=body_request)

    @allure.step('Шаг. Post запрос к API')
    def post_api_login(self, body_request: str):
        """Метод для отправки Post запроса, resourse - login

        Args:
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """

        url = f'{self.url}{self.resourse_login}'
        return Request().custom_request(method='POST', url=url, data=body_request)

    @allure.step('Шаг. Post запрос к API')
    def post_api_register(self, body_request: str):
        """Метод для отправки Post запроса, resourse - register

        Args:
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """

        url = f'{self.url}{self.resourse_register}'
        return Request().custom_request(method='POST', url=url, data=body_request)

    @allure.step('Шаг. DELETE запрос к API')
    def delete_api(self, id_user: str):
        """Метод для отправки Delete запроса

        Args:
            id_user: id пользователя

        Returns:
            Тело ответа
        """
        url = f'{self.url}{self.resourse_users}{id_user}'
        return Request().custom_request(method='DELETE', url=url)

    @allure.step('Шаг. PATCH запрос к API')
    def patch_api(self, id_user: str, body_request: str):
        """Метод для отправки Patch запроса

        Args:
            id_user: id пользователя
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """
        url = f'{self.url}{self.resourse_users}{id_user}'
        return Request().custom_request(method='PATCH', url=url, data=body_request)

    @allure.step('Шаг. PUT запрос к API')
    def put_api(self, id_user: str, body_request: str):
        """Метод для отправки Put запроса

        Args:
            id_user: id пользователя
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """
        url = f'{self.url}{self.resourse_users}{id_user}'
        return Request().custom_request(method='PUT', url=url, data=body_request)

