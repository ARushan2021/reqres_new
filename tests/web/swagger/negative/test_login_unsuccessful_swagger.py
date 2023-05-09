import allure
import pytest

from api.reqres.common import Common

from web.reqres.common import ReqresCommon
from web.swagger_reqres.steps_swagger_reqres import TestStepsSwaggerReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Negative keys')
@allure.epic('Web Тестирование swagger "https://reqres.in/api-docs/"')
@allure.title("Не успешный вход в систему")
@pytest.mark.parametrize('body_request',
                         [f'{Common.REQUEST_BODY_POST}',
                          f'{Common.REQUEST_BODY_POST2}'])
def test_login_unsuccessful(base, driver, screenshot, body_request):

    login_unsuccessful = TestStepsSwaggerReqres(driver, ReqresCommon.BASE_URL)
    web_response = login_unsuccessful.test_login_unsuccessful(body_request)
    response = base.api_v1.post_api_login(body_request)
    base.asserts.assert_web_and_api(api_response=response, web_response=web_response)
