import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres
from web.reqres.common import ReqresCommon


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Удаление пользователя")
def test_delete_user(driver):

    delete_user = TestStepsReqres(driver)
    delete_user.steps_delete_user()

