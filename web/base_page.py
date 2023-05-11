"""Модуль с базовыми методами на вэб страницах"""
import json

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from utils.asserts import AssertTests
from web.locators import LocatorsSwaggerReqres, LocatorsReqres
from web.common import ReqresCommon, SwaggerReqresCommon


class BasePage:
    """Класс для базовых метод на страницах"""

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.common_swag = SwaggerReqresCommon()
        self.locators_swag = LocatorsSwaggerReqres()
        self.common = ReqresCommon()
        self.locators = LocatorsReqres()

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
        """Метод для проверки загрузки странички. Если элемент найден на страничке, то код на паузе.
        Элемент проверяется в течение 30 сек.

            Args:
                locator: локатор для поиска на странице
                time: время в течение которого ищется локатор на странице
        """
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f'Страница не успела загрузиться!')

    def assert_title(self, exp_heading, locator_title):
        """Обертка для проверки заголовка странички

            Args:
                exp_heading: ожидаемый заголовок странички
                locator_title: локатор для поиска заголовка
        """
        heading_site = self.find_element(locator_title).text
        AssertTests.assert_web_heading(heading_site, exp_heading)

    def assert_web_page(self,
                        locator_state_code,
                        exp_status_code,
                        locator_response_body,
                        json_schema):
        """Обертка для проверки статус кода и json-схемы на reqres.ru

            Args:
                locator_state_code: локатор для поиска статус кода на страничке
                exp_status_code: ожидаемый статус код
                locator_response_body: локатор тела ответа
                json_schema: json-схема для проверки
        """
        status_code = self.find_element(locator_state_code).text
        AssertTests.check_status_code(status_code=int(status_code), exp_status_code=exp_status_code)
        response_body = self.find_element(locator_response_body).text
        response_body = response_body if len(response_body) < 3 else json.loads(response_body)
        AssertTests.validate_response_body(response_body=response_body, json_schema=json_schema)
