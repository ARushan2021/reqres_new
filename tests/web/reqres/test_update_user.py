import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Изменение всех параметров пользователя")
def test_update_user(driver):

    update_user = TestStepsReqres(driver)
    update_user.steps_update_user()
