"""Модуль содержит все декораторы проекта"""
import pytest
import os

from api.application import Application
from config import Config


@pytest.fixture(scope='session')
def base():
    """Декоратор по настройке только для API тестов"""
    return Application()


@pytest.fixture(scope='session')
def clear_test_reports_and_logs():
    """Декоратор по очистке каталогов logs и reports"""

    for f in os.listdir(Config.DIRECTORY_TEST_REPORTS):
        os.remove(os.path.join(Config.DIRECTORY_TEST_REPORTS, f))

    for c in os.listdir(Config.DIRECTORY_LOGS):
        os.remove(os.path.join(Config.DIRECTORY_LOGS, c))
