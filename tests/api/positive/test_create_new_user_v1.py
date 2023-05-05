"""Позитивный тест"""
import pytest
import allure

from schemas.post import Post
from api.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('body_request',
                         [f'{Common.REQUEST_BODY_POST}',
                          f'{Common.REQUEST_BODY_POST2}'])
@allure.title('Регистрация нового пользователя')
def test_single_user_v1(base, body_request):

    response = base.api_v1.post_api_users(body_request)
    base.asserts.assert_request(response=response, exp_status_code=201, json_schema=Post)

