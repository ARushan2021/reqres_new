"""Модуль с шагами по проверке"""
import json
import allure
from config import Config


class AssertTests:
    """Класс проверок для Тестов"""

    @staticmethod
    @allure.step('Проверка статус кода')
    def check_status_code(status_code, exp_status_code):
        """Метод проверки статус кода.
        Args:
            status_code: полученный статус код
            exp_status_code: ожидаемый статус код
        """

        msg = f'Статус код ответа "{status_code}" отличен от "{exp_status_code}"'
        assert int(status_code) == exp_status_code, msg

    @staticmethod
    @allure.step('Проверка схемы response body')
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
    @allure.step('Проверка времени ответа на запрос')
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

        AssertTests.check_status_code(status_code, exp_status_code)
        AssertTests.validate_response_body(response_body, json_schema)
        AssertTests.validate_time_response(response)

    @staticmethod
    @allure.step("Проверка заголовка странички")
    def assert_web_heading(heading_site: str, exp_heading: str):
        """Метод для проверки заголовка web-страницы

            Args:
                heading_site: полученный заголовок из web-страницы
                exp_heading: ожидаемый заголовок
            """
        assert heading_site == exp_heading, f'Не верный заголовок сайта: *{heading_site}*!'

    @staticmethod
    def assert_web_and_api(api_response, web_response):
        """Метод для сравнения статус кода и тела ответа на запрос API-запроса и аналогичного swagger запроса
            Ниже эти проверки разбиты на две, для того что-бы в allure было два шага проверка отдельно статус код,
            отдельно тело ответа

            Args:
                api_response: ответ полученный на api запрос
                web_response: список, содержащий статус код и тело ответа из web-странички
            """
        AssertTests.assert_st_code_web_and_api(api_response, web_response)
        AssertTests.assert_body_web_and_api(api_response, web_response)

    @staticmethod
    @allure.step("Проверка статус-кода")
    def assert_st_code_web_and_api(api_response, web_response):
        """Метод для сравнения статус кода ответа на запрос API-запроса и аналогичного swagger запроса

            Args:
                api_response: ответ полученный на api запрос
                web_response: список, содержащий статус код и тело ответа из web-странички
            """
        assert api_response.status_code == int(web_response[0]), \
            f'Статус код не верный! Из API запроса - {api_response.status_code}, Из WEB странички - {web_response[0]}'

    @staticmethod
    @allure.step("Проверка тела ответа на запрос")
    def assert_body_web_and_api(api_response, web_response):
        """Метод для сравнения тела ответа на запрос API-запроса и аналогичного swagger запроса

            Args:
                api_response: ответ полученный на api запрос
                web_response: список, содержащий статус код и тело ответа из web-странички
            """
        json_api_response_body = api_response.json()
        json_web_response_body = json.loads(web_response[1])
        assert json_api_response_body == json_web_response_body, \
            f'Body не совпадают!, Из API запроса: {json_api_response_body}, Из WEB странички: {json_web_response_body}'

