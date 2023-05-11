import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Изменение всех параметров пользователя")
def test_partial_update_user(driver):

    partial_update_user = TestStepsReqres(driver)
    partial_update_user.steps_partial_update_user()

