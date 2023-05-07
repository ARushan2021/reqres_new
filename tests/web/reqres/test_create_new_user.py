import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres
from web.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Регистрация нового пользователя")
def test_create_new_user(driver, screenshot):

    create_new_user = TestStepsReqres(driver, Common.BASE_URL)
    create_new_user.steps_create_new_user()
