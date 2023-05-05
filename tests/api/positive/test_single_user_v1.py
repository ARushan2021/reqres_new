"""Позитивный тест"""
import pytest
import allure
from schemas.get import Get


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['2',
                          '3'])
def test_single_user_v1(base, id_user):
    """Позитивный тест. Запрос информации о пользователе.

    Шаг 1. Отправка запроса. GET https://reqres.in/api/users/2
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    Шаг 4. Проверка времени ответа на запрос
    """

    response = base.api_v1.get_api_users(id_user=id_user)
    base.asserts.assert_request(response=response, exp_status_code=200, json_schema=Get)

