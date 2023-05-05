"""Модуль с шагами по проверке"""
import allure


class AssertApi:
    """Класс проверок для API"""

    @staticmethod
    @allure.step('Шаг. Проверка статус кода')
    def check_status_code(response, exp_status_code):
        """Метод проверки статус кода.

        Args:
            response: полученный ответ
            exp_status_code: ожидаемый статус код
        """
        # todo добавить шаг с allure или с логированием

        status_code = response.status_code
        msg = f'Статус код ответа "{status_code}" отличен от "{exp_status_code}"'
        assert int(status_code) == exp_status_code, msg

    @staticmethod
    @allure.step('Шаг. Проверка схемы response body')
    def validate_response_body(response, json_schema):
        """Метод валидации json-схемы тела ответа

        Args:
            response: полученный ответ
            json_schema: json-схема для валидации
        """

        if len(response.text) < 3:
            response_body = response.text
            assert response_body == json_schema, f'Тело ответа не верное: {response_body}'
        else:
            response_json = response.json()
            if isinstance(response_json, list):
                for item in response_json:
                    json_schema.parse_obj(item)
            else:
                json_schema.parse_obj(response_json)

    @staticmethod
    @allure.step('Шаг. Проверка времени ответа на запрос')
    def validate_time_response(response):
        """Метод для проверки времени ответа

        Args:
            response: полученный ответ
        """

        time_response = response.elapsed.total_seconds()
        assert time_response < 2, f'Ошибка! Время ответа на запрос превысило 2 сек. и составило: {time_response}'

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

        AssertApi.check_status_code(response, exp_status_code)
        AssertApi.validate_response_body(response, json_schema)
        AssertApi.validate_time_response(response)

