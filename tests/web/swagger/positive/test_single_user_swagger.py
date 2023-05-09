import allure
import pytest

from web.reqres.common import ReqresCommon
from web.swagger_reqres.steps_swagger_reqres import TestStepsSwaggerReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование swagger "https://reqres.in/api-docs/"')
@allure.title("Получение информации о пользователе")
@pytest.mark.parametrize('user_id',
                         ['2',
                          '3'])
def test_reqres_single_user_swagger(base, driver, screenshot, user_id):
    get_single_user = TestStepsSwaggerReqres(driver, ReqresCommon.BASE_URL)
    web_response = get_single_user.test_single_user(user_id)
    response = base.api_v1.get_api_users(user_id)
    base.asserts.assert_web_and_api(api_response=response, web_response=web_response)
