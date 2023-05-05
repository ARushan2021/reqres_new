"""Негативный тест"""
import pytest
import allure

from schemas.empty_request_body import EmptyRequestBody
from api.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Negative keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('body_request',
                         [f'{Common.REQUEST_BODY_POST}',
                          f'{Common.REQUEST_BODY_POST2}'])
@allure.title('Только что созданный пользователь не найден')
def test_new_user_not_found_v1(base, body_request):

    response_post = base.api_v1.post_api(body_request, res_api=Common.RESOURCE_USERS).json()
    response_get = base.api_v1.get_api(id_user=response_post['id'], res_api=Common.RESOURCE_USERS)
    base.asserts.assert_request(response=response_get, exp_status_code=404, json_schema=EmptyRequestBody.CURLY_BRACKETS)

