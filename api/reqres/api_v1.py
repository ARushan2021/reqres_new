"""Модуль содержит класс и методы с Api ручками"""
import allure

from .common import Common
from ..api_requests import Request


class ApiV1(Common):
    """Класс по работе с API"""

    def __init__(self):
        self.url = self.BASE_URL

    @allure.step('Шаг 1. Get запрос к апи')
    def get_api_users(self, id_user: int):
        """Метод для отправки Get запроса

        Args:
            id_user: id пользователя

        Returns:
            Тело ответа
        """

        url = f'{self.url}/api/users/{id_user}'
        return Request().custom_request(method='GET', url=url)

    @allure.step('Шаг 1. Post запрос к апи')
    def post_api_users(self, body_request: str):
        """Метод для отправки Post запроса

        Args:
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """

        url = f'{self.url}/api/users/'
        return Request().custom_request(method='POST', url=url, data=body_request)

    @allure.step('Шаг 1. DELETE запрос к апи')
    def delete_api_users(self, id_user: str):
        """Метод для отправки Post запроса

        Args:
            id_user: id пользователя

        Returns:
            Тело ответа
        """
        url = f'{self.url}/api/users/{id_user}'
        return Request().custom_request(method='DELETE', url=url)

    @allure.step('Шаг 1. PATCH запрос к апи')
    def patch_api_users(self, id_user: str, body_request: str):
        """Метод для отправки Post запроса

        Args:
            id_user: id пользователя
            body_request: тело запроса для отправки

        Returns:
            Тело ответа
        """
        url = f'{self.url}/api/users/{id_user}'
        return Request().custom_request(method='PATCH', url=url, data=body_request)

