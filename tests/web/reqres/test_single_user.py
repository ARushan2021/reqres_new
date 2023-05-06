import allure
import pytest

from steps_web.steps_reqres import Steps


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Проба")
def test_reqres_single_user(driver):

    get_single_user = Steps(driver, 'https://reqres.in/')
    get_single_user.open_page()
    get_single_user.get_single_user()
    get_single_user.assert_status_code()
    get_single_user.validate_response_body()
    get_single_user.validate_response_body()
