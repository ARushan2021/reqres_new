"""Модуль содержит класс и методы с Api ручками"""
import allure

from .common import Common
from ..api_requests import Request


class ApiV1(Common):
    """Класс по работе с API"""

    def __init__(self):
        self.url = self.BASE_URL

    @allure.step('Шаг. Get запрос к API')
    def get_api(self, id_user: int, res_api: str):
        """Метод для отправки Get запроса

        Args:
            id_user: id пользователя
            res_api: ресурс для url

        Returns:
            Тело ответа
        """
        url = f'{self.url}{res_api}{id_user}'
        return Request().custom_request(method='GET', url=url)

    @allure.step('Шаг. Post запрос к API')
    def post_api(self, body_request: str, res_api: str):
        """Метод для отправки Post запроса

        Args:
            body_request: тело запроса для отправки
            res_api: ресурс для url

        Returns:
            Тело ответа
        """

        url = f'{self.url}{res_api}'
        return Request().custom_request(method='POST', url=url, data=body_request)

    @allure.step('Шаг. DELETE запрос к API')
    def delete_api(self, id_user: str, res_api: str):
        """Метод для отправки Post запроса

        Args:
            id_user: id пользователя
            res_api: ресурс для url

        Returns:
            Тело ответа
        """
        url = f'{self.url}{res_api}{id_user}'
        return Request().custom_request(method='DELETE', url=url)

    @allure.step('Шаг. PATCH запрос к API')
    def patch_api(self, id_user: str, body_request: str, res_api: str):
        """Метод для отправки Post запроса

        Args:
            id_user: id пользователя
            body_request: тело запроса для отправки
            res_api: ресурс для url

        Returns:
            Тело ответа
        """
        url = f'{self.url}{res_api}{id_user}'
        return Request().custom_request(method='PATCH', url=url, data=body_request)

    @allure.step('Шаг. PUT запрос к API')
    def put_api(self, id_user: str, body_request: str, res_api: str):
        """Метод для отправки Post запроса

        Args:
            id_user: id пользователя
            body_request: тело запроса для отправки
            res_api: ресурс для url

        Returns:
            Тело ответа
        """
        url = f'{self.url}{res_api}{id_user}'
        return Request().custom_request(method='PUT', url=url, data=body_request)

