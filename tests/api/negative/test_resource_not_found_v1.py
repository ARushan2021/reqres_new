"""Негативный тест"""
import pytest
import allure

from schemas.empty_request_body import EmptyRequestBody
from api.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Negative keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['22',
                          '33'])
@allure.title('Неуспешный запрос информации о пользователе, неверный resource')
def test_resource_not_found_v1(base, id_user):

    response = base.api_v1.get_api(id_user=id_user, res_api=Common.RESOURCE_NOT_FOUND)
    base.asserts.assert_request(response=response, exp_status_code=404, json_schema=EmptyRequestBody.CURLY_BRACKETS)

