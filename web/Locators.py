from selenium.webdriver.common.by import By


class LocatorsReqres:

    GET_SINGLE_USER = (By.XPATH, '//li[@data-id="users-single"]')
    TITLE = (By.CSS_SELECTOR, '.tagline:nth-child(1)')
    SINGLE_USER_STATUS_CODE = (By.XPATH, '//span[@class="response-code"]')
    SINGLE_USER_RESPONSE_BODY = (By.XPATH, '//pre[@data-key="output-response"]')

