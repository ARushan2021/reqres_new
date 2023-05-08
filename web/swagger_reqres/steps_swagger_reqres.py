import time


from web.base_page import BasePage
from web.swagger_reqres.swagger_reqres_common import SwaggerReqresCommon
from web.Locators import LocatorsSwaggerReqres
import pyperclip
from api.api_requests import Request
from conftest import base

class TestStepsSwaggerReqres(BasePage):

    def test_single_user(self, user_id):
        BasePage.go_to_site(self, base_url=SwaggerReqresCommon.BASE_URL)
        BasePage.assert_title_swagger(self,
                                      exp_heading=SwaggerReqresCommon.EXP_HEADING,
                                      locator_title=LocatorsSwaggerReqres.TITLE)
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER).click()
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER_PARAMETERS).click()
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER_INPUT_PARAMETERS).send_keys(user_id)
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER_EXECUTE).click()
        time.sleep(1)  # поймать лоадинг
        single_user_status_code = self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER_STATUS_CODE).text
        self.find_element(locator=LocatorsSwaggerReqres.GET_SINGLE_USER_COPY_RESP_BODY).click()
        single_user_resp_bode = pyperclip.paste()
        assert_data = [single_user_status_code, single_user_resp_bode]
        print('*******')
        print(assert_data[0])
        print(assert_data[1])



        time.sleep(10)
