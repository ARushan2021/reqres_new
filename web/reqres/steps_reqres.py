import allure

from schemas.empty_request_body import EmptyRequestBody
from schemas.get import Get
from schemas.post import Post
from schemas.put_patch import PutPatch
from web.Locators import LocatorsReqres
from web.base_page import BasePage
from web.reqres.common import ReqresCommon


class BaseStepsReqres(BasePage):

    @allure.step("Нажатие кнопки 'Запроса'")
    def click_api_method(self, locator_button):
        self.find_element(locator_button).click()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.loading(locator=LocatorsReqres.LOADING)


class TestStepsReqres(BaseStepsReqres):

    def steps_get_single_user(self):
        BasePage.go_to_site(self, base_url=ReqresCommon.BASE_URL)
        BasePage.assert_title(self, exp_heading=ReqresCommon.EXP_HEADING, locator_title=LocatorsReqres.TITLE)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.GET_SINGLE_USER)
        BasePage.assert_web_page(self,
                                 locator_state_code=LocatorsReqres.STATUS_CODE,
                                 exp_status_code=200,
                                 locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                 json_schema=Get)

    def steps_create_new_user(self):
        BasePage.go_to_site(self, base_url=ReqresCommon.BASE_URL)
        BasePage.assert_title(self, exp_heading=ReqresCommon.EXP_HEADING, locator_title=LocatorsReqres.TITLE)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.CREATE_NEW_USER)
        BasePage.assert_web_page(self,
                                 locator_state_code=LocatorsReqres.STATUS_CODE,
                                 exp_status_code=201,
                                 locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                 json_schema=Post)

    def steps_delete_user(self):
        BasePage.go_to_site(self, base_url=ReqresCommon.BASE_URL)
        BasePage.assert_title(self, exp_heading=ReqresCommon.EXP_HEADING, locator_title=LocatorsReqres.TITLE)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.DELETE_USER)
        BasePage.assert_web_page(self,
                                 locator_state_code=LocatorsReqres.STATUS_CODE,
                                 exp_status_code=204,
                                 locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                 json_schema=EmptyRequestBody.EMPTY_STR)

    def steps_update_user(self):
        BasePage.go_to_site(self, base_url=ReqresCommon.BASE_URL)
        BasePage.assert_title(self, exp_heading=ReqresCommon.EXP_HEADING, locator_title=LocatorsReqres.TITLE)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.UPDATE_USER)
        BasePage.assert_web_page(self,
                                 locator_state_code=LocatorsReqres.STATUS_CODE,
                                 exp_status_code=200,
                                 locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                 json_schema=PutPatch)

    def steps_partial_update_user(self):
        BasePage.go_to_site(self, base_url=ReqresCommon.BASE_URL)
        BasePage.assert_title(self, exp_heading=ReqresCommon.EXP_HEADING, locator_title=LocatorsReqres.TITLE)
        BaseStepsReqres.click_api_method(self, locator_button=LocatorsReqres.PATCH_UPDATE_USER)
        BasePage.assert_web_page(self,
                                 locator_state_code=LocatorsReqres.STATUS_CODE,
                                 exp_status_code=200,
                                 locator_response_body=LocatorsReqres.RESPONSE_BODY,
                                 json_schema=PutPatch)
