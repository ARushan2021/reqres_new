import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres
from web.reqres.common import ReqresCommon


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Получение информации о пользователе")
def test_reqres_single_user(driver, screenshot):

    get_single_user = TestStepsReqres(driver, ReqresCommon.BASE_URL)
    get_single_user.steps_get_single_user()
