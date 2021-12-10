from locators import AlertM


class AlertMessage:

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element_by_css_selector(AlertM.success.login['css']).click()

    def click_to_cart(self):
        self.driver.find_element_by_css_selector(AlertM.success.to_cart['css']).click()
