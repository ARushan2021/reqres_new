"""Позитивный тест"""
import pytest
import allure

from schemas.get import Get
from api.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['2',
                          '3'])
@allure.title('Получение информации о пользователе')
def test_single_user_v1(base, id_user):

    response = base.api_v1.get_api(id_user=id_user, res_api=Common.RESOURCE_USERS)
    base.asserts.assert_request(response=response, exp_status_code=200, json_schema=Get)

