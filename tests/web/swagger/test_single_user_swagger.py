import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres
from web.reqres.common import ReqresCommon
from web.swagger_reqres.steps_swagger_reqres import TestStepsSwaggerReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Получение информации о пользователе")
def test_reqres_single_user_swagger(base, driver, screenshot):

    get_single_user = TestStepsSwaggerReqres(driver, ReqresCommon.BASE_URL)
    get_single_user.test_single_user('2')
    # response = base.api_v1.get_api_users(id_user='2')
    # assert response.status_code ==


