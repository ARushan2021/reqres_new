"""Методы для проверки ответов на запросы"""


class Checking:

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response_result, expected_status_code):
        Checking.expected_status_code = expected_status_code
        assert response_result.status_code == int(Checking.expected_status_code), \
            f'Получен не верный статус код {response_result.status_code}'

    """Валидация json-схемы тела ответа"""
    @staticmethod
    def validate_response_body(response_result, json_schema):
        if len(response_result.text) < 3:
            response_body = response_result.text
            assert response_body == json_schema, f'Тело ответа не верное: {response_body}'
        else:
            response_json = response_result.json()
            if isinstance(response_json, list):
                for item in response_json:
                    json_schema.parse_obj(item)
            else:
                json_schema.parse_obj(response_json)

    """Проверка времени ответа"""
    @staticmethod
    def validate_time_response(response_result):
        time_response = response_result.elapsed.total_seconds()
        assert time_response < 2, f'Ошибка! Время ответа на запрос превысило 2 сек. и составило: {time_response}'

    @staticmethod
    def checking_request(response_result, expected_status_code, json_schema):
        Checking.check_status_code(response_result, expected_status_code)
        Checking.validate_response_body(response_result, json_schema)
        Checking.validate_time_response(response_result)

