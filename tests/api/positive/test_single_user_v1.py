"""Позитивный тест"""
import allure
import pytest

from schemas.get import Get


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['2',
                          '3'])
@allure.title('Получение информации о пользователе')
def test_single_user_v1(base, id_user):
    response = base.api_v1.get_api_users(id_user=id_user)
    base.asserts.assert_request(response=response, exp_status_code=200, json_schema=Get)
