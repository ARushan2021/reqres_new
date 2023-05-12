"""Модуль с шагами по тестированию swagger reqres.ru"""

import allure
import pyperclip

from utils.asserts import AssertTests
from web.base_page import BasePage
from web.swagger_reqres.common import SwaggerReqresCommon
from web.swagger_reqres.locators import LocatorsSwaggerReqres


class TestStepsSwaggerReqres(BasePage):
    """Класс с шагами по тестированию swagger reqres.ru"""

    def __init__(self, driver):
        super().__init__(driver)
        self.common_swag = SwaggerReqresCommon()
        self.locators_swag = LocatorsSwaggerReqres()

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

        self.go_to_site(base_url=self.common_swag.BASE_URL)
        self.assert_title_swagger(exp_heading=self.common_swag.EXP_HEADING, locator_title=self.locators_swag.TITLE)
        self.find_element(locator=self.locators_swag.GET_SINGLE_USER).click()
        self.loading(self.locators_swag.LOADING_BLOCK)
        self.find_element(locator=self.locators_swag.TRY_IT_OUT_BUTTON).click()
        self.find_element(locator=self.locators_swag.GET_SINGLE_USER_INPUT_PARAMETERS).send_keys(user_id)
        self.find_element(locator=self.locators_swag.EXECUTE_BUTTON).click()
        self.loading(self.locators_swag.LOADING_EXECUTE)
        single_user_st_code = self.find_element(locator=self.locators_swag.STATUS_CODE).text
        self.find_element(locator=self.locators_swag.COPY_RESP_BODY).click()
        single_user_resp_bode = pyperclip.paste()
        web_response = [single_user_st_code, single_user_resp_bode]

        return web_response

    @allure.step('Отправка запроса через WEB-страничку')
    def test_login_unsuccessful(self, body_request):
        """Метод для тестирования неуспешного входа в систему"""

        self.go_to_site(base_url=self.common_swag.BASE_URL)
        self.assert_title_swagger(exp_heading=self.common_swag.EXP_HEADING, locator_title=self.locators_swag.TITLE)
        self.find_element(locator=self.locators_swag.POST_LOGIN).click()
        self.loading(self.locators_swag.LOADING_BLOCK)
        self.find_element(locator=self.locators_swag.TRY_IT_OUT_BUTTON).click()
        self.find_element(locator=self.locators_swag.POST_LOGIN_INPUT_RQ_BODY).clear()
        self.find_element(locator=self.locators_swag.POST_LOGIN_INPUT_RQ_BODY).send_keys(body_request)
        self.find_element(locator=self.locators_swag.EXECUTE_BUTTON).click()
        self.loading(self.locators_swag.LOADING_EXECUTE)
        login_unsuccessful_st_code = self.find_element(locator=self.locators_swag.STATUS_CODE).text
        self.find_element(locator=self.locators_swag.COPY_RESP_BODY2).click()
        login_unsuccessful_resp_bode = pyperclip.paste()
        web_response = [login_unsuccessful_st_code, login_unsuccessful_resp_bode]

        return web_response
