import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres
from web.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Удаление пользователя")
def test_delete_user(driver, screenshot):

    delete_user = TestStepsReqres(driver, Common.BASE_URL)
    delete_user.steps_delete_user()

