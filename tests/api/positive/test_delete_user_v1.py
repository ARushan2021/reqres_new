"""Позитивный тест"""
import pytest
import allure
from schemas.empty_request_body import EmptyRequestBody


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['20',
                          '32'])
def test_delete_user_v1(base, id_user):
    """Позитивный тест. Удаление пользователя.

    Шаг 1. Отправка запроса. DELETE https://reqres.in/api/users/20
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    Шаг 4. Проверка времени ответа на запрос
    """

    response = base.api_v1.delete_api_users(id_user=id_user)
    base.asserts.assert_request(response=response, exp_status_code=204, json_schema=EmptyRequestBody.EMPTY_STR)

