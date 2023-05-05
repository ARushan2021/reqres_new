"""Модуль содержит все константы"""


class Common:
    BASE_URL = 'https://reqres.in'

    RESOURCE_USERS = '/api/users/'
    RESOURCE_LOGIN = '/api/login/'
    RESOURCE_NOT_FOUND = '/api/unknown/'
    RESOURCE_REGISTER = '/api/register/'

    DIRECTORY_LOGS = 'logs/'
    DIRECTORY_TEST_REPORTS = 'test_reports/'

    REQUEST_BODY_POST = '{"first_name": "morpheus","email": "mushroom@yandex.ru"}'
    REQUEST_BODY_POST2 = '{"first_name": "Testers","email": "mus@hr.oom"}'
    REQUEST_BODY_UPDATE = '{"first_name": "Testers","second_name": "second"}'
    REQUEST_BODY_UPDATE2 = '{"first_name": "Testers","job": "IBS"}'


