"""Негативный тест"""
import pytest
import allure

from schemas.post import PostUnseccessful
from api.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Negative keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('body_request',
                         [f'{Common.REQUEST_BODY_POST}',
                          f'{Common.REQUEST_BODY_POST2}'])
@allure.title('Неуспешная регистрация нового пользователя')
def test_login_unsuccessful_v1(base, body_request):

    response = base.api_v1.post_api_register(body_request)
    base.asserts.assert_request(response=response, exp_status_code=400, json_schema=PostUnseccessful)

