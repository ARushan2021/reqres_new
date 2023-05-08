"""Модуль с шагами по проверке"""
import allure
from config import Config


class AssertApi:
    """Класс проверок для API"""

    @staticmethod
    @allure.step('Шаг. Проверка статус кода')
    def check_status_code(status_code, exp_status_code):
        """Метод проверки статус кода.
        Args:
            status_code: полученный статус код
            exp_status_code: ожидаемый статус код
        """

        msg = f'Статус код ответа "{status_code}" отличен от "{exp_status_code}"'
        assert int(status_code) == exp_status_code, msg

    @staticmethod
    @allure.step('Шаг. Проверка схемы response body')
    def validate_response_body(response_body, json_schema):
        """Метод валидации json-схемы тела ответа
        Args:
            response_body: тело полученного ответа
            json_schema: json-схема для валидации
        """

        if isinstance(response_body, str):
            assert response_body == json_schema, f'Тело ответа не верное: {response_body}'
        else:
            json_schema.parse_obj(response_body)

    @staticmethod
    @allure.step('Шаг. Проверка времени ответа на запрос')
    def validate_time_response(response):
        """Метод для проверки времени ответа
        Args:
            response: полученный ответ
        """

        time_response = response.elapsed.total_seconds()
        assert time_response < Config.TIME_RESPONSE, f'Ошибка! Время ответа на запрос превысило 2 сек. и составило: {time_response}'

    @staticmethod
    def assert_request(response, exp_status_code, json_schema):
        """Метод объединят три проверки ответа
            - статус кода
            - валидации json-схемы
            - проверка времени ответа
        Args:
            response: полученный ответ
            exp_status_code: ожидаемый статус код
            json_schema: json-схема для валидации
        """

        if len(response.text) < 3:
            response_body = response.text
        else:
            response_body = response.json()

        status_code = response.status_code

        AssertApi.check_status_code(status_code, exp_status_code)
        AssertApi.validate_response_body(response_body, json_schema)
        AssertApi.validate_time_response(response)

    @staticmethod
    @allure.step("Проверка заголовка странички")
    def assert_web_heading(heading_site: str, exp_heading: str):
        assert heading_site == exp_heading, f'Не верный заголовок сайта: *{heading_site}*!'
