import time

import allure
import pyperclip

from web.Locators import LocatorsSwaggerReqres
from web.base_page import BasePage
from web.swagger_reqres.common_swagger import SwaggerReqresCommon


class TestStepsSwaggerReqres(BasePage):

    @allure.step('Отправка запроса через WEB-страничку')
    def test_single_user(self, user_id: str):
        BasePage.go_to_site(self, base_url=SwaggerReqresCommon.BASE_URL)
        BasePage.assert_title_swagger(self,
                                      exp_heading=SwaggerReqresCommon.EXP_HEADING,
                                      locator_title=LocatorsSwaggerReqres.TITLE)
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER).click()
        self.find_element(locator=LocatorsSwaggerReqres.TRY_IT_OUT_BUTTON).click()
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER_INPUT_PARAMETERS).send_keys(user_id)
        self.find_element(locator=LocatorsSwaggerReqres.EXECUTE_BUTTON).click()
        time.sleep(1)  # поймать loading
        single_user_st_code = self.find_element(locator=LocatorsSwaggerReqres.STATUS_CODE).text
        self.find_element(locator=LocatorsSwaggerReqres.COPY_RESP_BODY).click()
        single_user_resp_bode = pyperclip.paste()
        web_response = [single_user_st_code, single_user_resp_bode]

        return web_response

    @allure.step('Отправка запроса через WEB-страничку')
    def test_login_unsuccessful(self, body_request):
        BasePage.go_to_site(self, base_url=SwaggerReqresCommon.BASE_URL)
        BasePage.assert_title_swagger(self,
                                      exp_heading=SwaggerReqresCommon.EXP_HEADING,
                                      locator_title=LocatorsSwaggerReqres.TITLE)
        self.find_element(locator=LocatorsSwaggerReqres.POST_LOGIN).click()
        self.find_element(locator=LocatorsSwaggerReqres.TRY_IT_OUT_BUTTON).click()
        self.find_element(locator=LocatorsSwaggerReqres.POST_LOGIN_INPUT_RQ_BODY).clear()
        self.find_element(locator=LocatorsSwaggerReqres.POST_LOGIN_INPUT_RQ_BODY).send_keys(body_request)
        self.find_element(locator=LocatorsSwaggerReqres.EXECUTE_BUTTON).click()
        time.sleep(2) # поймать loading
        login_unsuccessful_st_code = self.find_element(locator=LocatorsSwaggerReqres.STATUS_CODE).text
        self.find_element(locator=LocatorsSwaggerReqres.COPY_RESP_BODY2).click()
        login_unsuccessful_resp_bode = pyperclip.paste()
        web_response = [login_unsuccessful_st_code, login_unsuccessful_resp_bode]

        return web_response
