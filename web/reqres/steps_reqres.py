import json

import allure
from web.Locators import LocatorsReqres

from web.base_page import BasePage
from utils.asserts import AssertApi
from schemas.post import Post
from schemas.get import Get
from schemas.put_patch import PutPatch
from schemas.empty_request_body import EmptyRequestBody
from web.reqres.common import Common


class BaseStepsReqres(BasePage):

    @allure.step("Открытие странички")
    def open_page(self):
        self.go_to_site()
        heading_site = self.find_element(LocatorsReqres.TITLE).text
        AssertApi.assert_web_heading(heading_site=heading_site, exp_heading=Common.EXP_HEADING)

    @allure.step("Нажатие кнопки 'Запроса'")
    def click_api_method(self, locator_button):
        self.find_element(locator_button).click()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.loading(locator=LocatorsReqres.LOADING)

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


class TestStepsReqres(BaseStepsReqres):

    def steps_get_single_user(self):
        BaseStepsReqres.open_page(self)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.GET_SINGLE_USER)
        BaseStepsReqres.assert_web_page(self,
                                        locator_state_code=LocatorsReqres.STATUS_CODE,
                                        exp_status_code=200,
                                        locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                        json_schema=Get)

    def steps_create_new_user(self):
        BaseStepsReqres.open_page(self)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.CREATE_NEW_USER)
        BaseStepsReqres.assert_web_page(self,
                                        locator_state_code=LocatorsReqres.STATUS_CODE,
                                        exp_status_code=201,
                                        locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                        json_schema=Post)

    def steps_delete_user(self):
        BaseStepsReqres.open_page(self)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.DELETE_USER)
        BaseStepsReqres.assert_web_page(self,
                                        locator_state_code=LocatorsReqres.STATUS_CODE,
                                        exp_status_code=204,
                                        locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                        json_schema=EmptyRequestBody.EMPTY_STR)

    def steps_update_user(self):
        BaseStepsReqres.open_page(self)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.UPDATE_USER)
        BaseStepsReqres.assert_web_page(self,
                                        locator_state_code=LocatorsReqres.STATUS_CODE,
                                        exp_status_code=200,
                                        locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                        json_schema=PutPatch)

    def steps_partial_update_user(self):
        BaseStepsReqres.open_page(self)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.PATCH_UPDATE_USER)
        BaseStepsReqres.assert_web_page(self,
                                        locator_state_code=LocatorsReqres.STATUS_CODE,
                                        exp_status_code=200,
                                        locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                        json_schema=PutPatch)

