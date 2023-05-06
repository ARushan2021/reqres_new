import json
import time

import allure
from selenium.webdriver.common.by import By
from locators.Locators import LocatorsReqres

from steps_web.base_page import BasePage
from utils.asserts import AssertApi
from schemas.get import Get


class Steps(BasePage):

    @allure.step("Открытие странички")
    def open_page(self):
        self.go_to_site()
        heading_site = self.find_element(LocatorsReqres.TITLE).text
        AssertApi.checking_heading(heading_site=heading_site, exp_heading='Test your front-end against a real API')

    @allure.step("Нажимаем на кнопку 'Single User'")
    def get_single_user(self):
        self.find_element(LocatorsReqres.GET_SINGLE_USER).click()

    @allure.step("Проверка статус кода на странице")
    def assert_status_code(self):
        status_code = self.find_element(LocatorsReqres.SINGLE_USER_STATUS_CODE).text
        AssertApi.check_status_code(status_code=int(status_code), exp_status_code=200)

    @allure.step("Проверка Json-схемы полученной на странице")
    def validate_response_body(self):
        response_body = self.find_element(LocatorsReqres.SINGLE_USER_RESPONSE_BODY).text
        json_response_body = json.loads(response_body)
        AssertApi.validate_response_body(response_body=json_response_body, json_schema=Get)

