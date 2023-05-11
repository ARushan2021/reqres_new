"""Модуль с шагами по тестированию reqres.ru"""
import allure

from schemas.empty_request_body import EmptyRequestBody
from schemas.get import Get
from schemas.post import Post
from schemas.put_patch import PutPatch
from web.locators import LocatorsReqres
from web.base_page import BasePage
from web.common import ReqresCommon


class BaseStepsReqres(BasePage):
    """Класс с базовыми шагами по тестированию reqres.ru"""

    # def __init__(self, driver):
    #     self.common = ReqresCommon()
    #     self.locators = LocatorsReqres()
    #     super(BaseStepsReqres, self).__init__(driver)

    @allure.step("Нажатие кнопки 'Запроса'")
    def click_api_method(self, locator_button):
        """Метод для нажатия нужного api-метода и скроллинг странички"""
        self.find_element(locator_button).click()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.loading(locator=LocatorsReqres.LOADING)


class TestStepsReqres(BaseStepsReqres):
    """Класс с шагами по тестированию reqres.ru"""

    def steps_get_single_user(self):
        """Метод для тестирования получения информации о пользователе"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.click_api_method(locator_button=self.locators.GET_SINGLE_USER)
        self.assert_web_page(locator_state_code=self.locators.STATUS_CODE,
                             exp_status_code=200,
                             locator_response_body=self.locators.RESPONSE_BODY,
                             json_schema=Get)

    def steps_create_new_user(self):
        """Метод для тестирования создания нового пользователя"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.click_api_method(locator_button=self.locators.CREATE_NEW_USER)
        self.assert_web_page(locator_state_code=self.locators.STATUS_CODE,
                             exp_status_code=201,
                             locator_response_body=self.locators.RESPONSE_BODY,
                             json_schema=Post)

    def steps_delete_user(self):
        """Метод для тестирования удаления пользователя"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.click_api_method(locator_button=self.locators.DELETE_USER)
        self.assert_web_page(locator_state_code=self.locators.STATUS_CODE,
                             exp_status_code=204,
                             locator_response_body=self.locators.RESPONSE_BODY,
                             json_schema=EmptyRequestBody.EMPTY_STR)

    def steps_update_user(self):
        """Метод для тестирования обновления всего пользователя"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.click_api_method(locator_button=self.locators.UPDATE_USER)
        self.assert_web_page(locator_state_code=self.locators.STATUS_CODE,
                             exp_status_code=200,
                             locator_response_body=self.locators.RESPONSE_BODY,
                             json_schema=PutPatch)

    def steps_partial_update_user(self):
        """Метод для тестирования частичного обновления пользователя"""

        self.go_to_site(base_url=self.common.BASE_URL)
        self.assert_title(exp_heading=self.common.EXP_HEADING, locator_title=self.locators.TITLE)
        self.click_api_method(locator_button=self.locators.PATCH_UPDATE_USER)
        self.assert_web_page(locator_state_code=self.locators.STATUS_CODE,
                             exp_status_code=200,
                             locator_response_body=self.locators.RESPONSE_BODY,
                             json_schema=PutPatch)
