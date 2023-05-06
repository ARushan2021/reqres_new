import allure
import pytest

from web.reqres.steps_reqres import Steps
from web.reqres.common import Common


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Получение информации о пользователе")
def test_reqres_single_user(driver):

    get_single_user = Steps(driver, Common.BASE_URL)
    get_single_user.open_page()
    get_single_user.get_single_user()
    get_single_user.assert_status_code()
    get_single_user.validate_response_body()
