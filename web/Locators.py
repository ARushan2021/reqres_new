from selenium.webdriver.common.by import By


class LocatorsReqres:

    TITLE = (By.CSS_SELECTOR, '.tagline:nth-child(1)')
    STATUS_CODE = (By.XPATH, '//span[@data-key="response-code"]')
    RESPONSE_BODY = (By.XPATH, '//pre[@data-key="output-response"]')
    LOADING = (By.XPATH, '//div[@data-key="spinner"]')

    GET_SINGLE_USER = (By.XPATH, '//li[@data-id="users-single"]')
    CREATE_NEW_USER = (By.XPATH, '//li[@data-id="post"]')
    DELETE_USER = (By.XPATH, '//li[@data-id="delete"]')
    UPDATE_USER = (By.XPATH, '//li[@data-id="put"]')
    PATCH_UPDATE_USER = (By.XPATH, '//li[@data-id="patch"]')


class LocatorsSwaggerReqres:
    TITLE = (By.XPATH, '//h2[@class="title"]')

    GET_SINGLE_USER = (By.CSS_SELECTOR, '#operations-default-get_users__id_ > div > button > svg')
    GET_SINGLE_USER_PARAMETERS = (By.CSS_SELECTOR, 'div.opblock-section-header > div.try-out > button')
    GET_SINGLE_USER_INPUT_PARAMETERS = (By.CSS_SELECTOR, 'td.parameters-col_description > input[type=text]')
    GET_SINGLE_USER_EXECUTE = (By.CSS_SELECTOR, 'div.execute-wrapper > button')
    GET_SINGLE_USER_STATUS_CODE = \
        (By.CSS_SELECTOR, 'div.responses-inner > div > div > table > tbody > tr > td.response-col_status')
    GET_SINGLE_USER_COPY_RESP_BODY = \
        (By.CSS_SELECTOR, 'td.response-col_description > div:nth-child(1) > div > div.copy-to-clipboard > button')

