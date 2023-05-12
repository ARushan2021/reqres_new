"""Модуль с локаторами для swagger reqres"""
from selenium.webdriver.common.by import By


class LocatorsSwaggerReqres:
    """Локаторы для работы с swagger"""

    TITLE = (By.XPATH, '//h2[@class="title"]')
    TRY_IT_OUT_BUTTON = (By.CSS_SELECTOR, 'div.opblock-section-header > div.try-out > button')
    EXECUTE_BUTTON = (By.CSS_SELECTOR, 'div.execute-wrapper > button')
    STATUS_CODE = \
        (By.CSS_SELECTOR, 'div.responses-inner>div>div>table>tbody>tr>td.response-col_status')
    COPY_RESP_BODY = \
        (By.CSS_SELECTOR, 'td.response-col_description>div:nth-child(1)>div>div.copy-to-clipboard>button')
    COPY_RESP_BODY2 = \
        (By.CSS_SELECTOR, 'div:nth-child(2)>div>div.copy-to-clipboard>button')
    LOADING_EXECUTE = (By.CSS_SELECTOR, 'div.loading-container>div.loading')
    LOADING_BLOCK = (By.CSS_SELECTOR, 'div.no-margin>div>img.opblock-loading-animation')

    GET_SINGLE_USER = (By.CSS_SELECTOR, '#operations-default-get_users__id_ > div > button > svg')
    GET_SINGLE_USER_INPUT_PARAMETERS = (By.CSS_SELECTOR, 'td.parameters-col_description > input[type=text]')

    POST_LOGIN = (By.CSS_SELECTOR, '#operations-default-post_login > div > button > svg')
    POST_LOGIN_INPUT_RQ_BODY = (By.CSS_SELECTOR, 'div.opblock-description-wrapper>div>div>div>textarea')