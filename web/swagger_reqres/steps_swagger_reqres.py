"""Модуль с шагами по тестированию swagger reqres.ru"""

import allure
import pyperclip

from utils.asserts import AssertTests
from web.Locators import LocatorsSwaggerReqres
from web.base_page import BasePage
from web.swagger_reqres.common_swagger import SwaggerReqresCommon


class TestStepsSwaggerReqres(BasePage):
    """Класс с шагами по тестированию swagger reqres.ru"""

    def __init__(self, driver):
        self.common = SwaggerReqresCommon()
        self.locators = LocatorsSwaggerReqres()
        super(TestStepsSwaggerReqres, self).__init__(driver)

    def assert_title_swagger(self, exp_heading, locator_title):
        """Обертка для проверки заголовка странички swagger

            Args:
                exp_heading: ожидаемый заголовок странички
                locator_title: локатор для поиска заголовка
        """
        heading_site = self.find_element(locator_title).text
        heading_site = heading_site[0: 10]
        AssertTests.assert_web_heading(heading_site, exp_heading)

    @allure.step('Отправка запроса через WEB-страничку')
    def test_single_user(self, user_id: str):
        """Метод для тестирования получения информации о пользователе"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title_swagger(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.find_element(locator=self.locators.GET_SINGLE_USER).click()
        self.loading(self.locators.LOADING_BLOCK)
        self.find_element(locator=self.locators.TRY_IT_OUT_BUTTON).click()
        self.find_element(locator=self.locators.GET_SINGLE_USER_INPUT_PARAMETERS).send_keys(user_id)
        self.find_element(locator=self.locators.EXECUTE_BUTTON).click()
        self.loading(self.locators.LOADING_EXECUTE)
        single_user_st_code = self.find_element(locator=self.locators.STATUS_CODE).text
        self.find_element(locator=self.locators.COPY_RESP_BODY).click()
        single_user_resp_bode = pyperclip.paste()
        web_response = [single_user_st_code, single_user_resp_bode]

        return web_response

    @allure.step('Отправка запроса через WEB-страничку')
    def test_login_unsuccessful(self, body_request):
        """Метод для тестирования неуспешного входа в систему"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title_swagger(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.find_element(locator=self.locators.POST_LOGIN).click()
        self.loading(self.locators.LOADING_BLOCK)
        self.find_element(locator=self.locators.TRY_IT_OUT_BUTTON).click()
        self.find_element(locator=self.locators.POST_LOGIN_INPUT_RQ_BODY).clear()
        self.find_element(locator=self.locators.POST_LOGIN_INPUT_RQ_BODY).send_keys(body_request)
        self.find_element(locator=self.locators.EXECUTE_BUTTON).click()
        self.loading(self.locators.LOADING_EXECUTE)
        login_unsuccessful_st_code = self.find_element(locator=self.locators.STATUS_CODE).text
        self.find_element(locator=self.locators.COPY_RESP_BODY2).click()
        login_unsuccessful_resp_bode = pyperclip.paste()
        web_response = [login_unsuccessful_st_code, login_unsuccessful_resp_bode]

        return web_response
