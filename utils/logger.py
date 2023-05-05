import datetime
import os


"""Запись логов к запросам"""


class Logger:
    file_name = f'logs/log_{str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.log'

    @classmethod
    def write_log_to_file(cls, data: str, ):
        """Создание и запись информации в файл лога"""

        with open(cls.file_name, "a", encoding="utf-8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, request):
        """Сбор информации по request"""

        test_name = os.environ.get("PYTEST_CURRENT_TEST")

        data_to_add = f'\n***************\n'
        data_to_add += '\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Request method: {request.request.method}\n'
        data_to_add += f'Request URL: {request.request.url}\n'
        data_to_add += f'Request body: {request.request.body}\n'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response):
        """Сбор информации по response"""

        headers_as_dict = dict(response.headers)
        cookies_as_dict = dict(response.cookies)

        data_to_add = f'Response status code: {response.status_code}\n'
        data_to_add += f'Response body: {response.text}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'

        cls.write_log_to_file(data_to_add)

    @staticmethod
    def logging(response):
        """Метод логирования ответов и запросов"""

        Logger.add_request(request=response)
        Logger.add_response(response=response)


