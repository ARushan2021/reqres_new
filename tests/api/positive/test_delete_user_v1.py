"""Позитивный тест"""
import pytest
import allure

from api.reqres.common import Common
from schemas.empty_request_body import EmptyRequestBody


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['20',
                          '32'])
@allure.title('Удаление пользователя')
def test_delete_user_v1(base, id_user):

    response = base.api_v1.delete_api(id_user=id_user, res_api=Common.RESOURCE_USERS)
    base.asserts.assert_request(response=response, exp_status_code=204, json_schema=EmptyRequestBody.EMPTY_STR)

