"""Модуль содержит все декораторы проекта"""

import pytest
import os
import allure

from api.application import Application
from config import Config
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture(scope='session')
def base():
    """Декоратор по настройке только для API тестов"""
    return Application()


@pytest.fixture(scope='session')
def clear_test_reports_and_logs():
    """Декоратор по очистке каталогов logs и reports"""

    f = os.listdir(Config.DIRECTORY_TEST_REPORTS)
    f.remove('environment.properties')
    for i in range(0, len(f)):
        os.remove(f'{Config.DIRECTORY_TEST_REPORTS}/{f[i]}')

    for c in os.listdir(Config.DIRECTORY_LOGS):
        os.remove(os.path.join(Config.DIRECTORY_LOGS, c))


@pytest.fixture(scope='session')
def driver():
    """Декоратор для открытия страницы в браузере. И закрытия браузера после окончания сессии"""

    driver = webdriver.Chrome(Config.DIRECTORY_DRIVER_CHROME)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def screenshot(driver):
    """Декоратор для скриншота после каждой функции"""

    yield
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)






