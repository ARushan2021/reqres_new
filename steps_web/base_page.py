"""Модуль с базовыми методам на вэб страницах"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import Config


class BasePage:
    """Класс для базовых метод на страницах"""

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def go_to_site(self):
        """Метод для открытия сайта"""

        self.driver.get(self.base_url)

    def find_element(self, locator, time=Config.LOCATOR_SEARCH_TIME):
        """Метод для поиска локатора на странице.
        Если локатор не нашелся в течение заданного времени, то выкидывает ошибку.

        Args:
            locator: локатор для поиска на странице
            time: время в течение которого ищется локатор на странице

        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент по локатору {locator}")

