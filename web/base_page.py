"""Модуль с базовыми методам на вэб страницах"""
import json
import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from utils.asserts import AssertApi


class BasePage:
    """Класс для базовых метод на страницах"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @allure.step("Открытие странички")
    def go_to_site(self, base_url):
        """Метод для открытия сайта"""

        self.driver.get(base_url)

    def find_element(self, locator, time=Config.LOCATOR_SEARCH_TIME):
        """Метод для поиска локатора на странице.
        Если локатор не нашелся в течение заданного времени, то выкидывает ошибку.

        Args:
            locator: локатор для поиска на странице
            time: время в течение которого ищется локатор на странице

        """

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент по локатору {locator}")

    def loading(self, locator, time=Config.LOCATOR_SEARCH_TIME):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f'Страница не успела загрузиться!')

    def assert_title(self, exp_heading, locator_title):
        heading_site = self.find_element(locator_title).text
        AssertApi.assert_web_heading(heading_site, exp_heading)

    def assert_title_swagger(self, exp_heading, locator_title):
        heading_site = self.find_element(locator_title).text
        heading_site = heading_site[0: 10]
        AssertApi.assert_web_heading(heading_site, exp_heading)

    def assert_web_page(self,
                        locator_state_code,
                        exp_status_code,
                        locator_response_body,
                        json_schema):
        status_code = self.find_element(locator_state_code).text
        AssertApi.check_status_code(status_code=int(status_code), exp_status_code=exp_status_code)
        response_body = self.find_element(locator_response_body).text
        if len(response_body) < 3:
            response_body = response_body
        else:
            response_body = json.loads(response_body)
        AssertApi.validate_response_body(response_body=response_body, json_schema=json_schema)
