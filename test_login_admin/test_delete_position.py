from selenium.webdriver.common.alert import Alert

from locators import LoginAdmin, ProductPage


def test_delete_position(browser, request):
    url = ""
    browser.get("".join([request.config.getoption("--url"), url]))
    browser.find_element_by_css_selector(LoginAdmin.username).send_keys("admin")
    browser.find_element_by_css_selector(LoginAdmin.password).send_keys("admin")
    browser.find_element_by_css_selector(LoginAdmin.submit).click()
    browser.find_element_by_css_selector("button.close").click()
    browser.find_element_by_css_selector("a.parent").click()
    catalog_elements = browser.find_elements_by_css_selector(".collapse.in > li")
    for catalog_element in catalog_elements:
        if catalog_element.text == "Products":
            catalog_element.click()
            break
    browser.find_element_by_xpath("//*[@id='form-product']/div/table/tbody/tr[19]/td[1]/input").click()
    browser.find_element_by_css_selector(ProductPage.delete_position).click()
    Alert(browser).accept()
    notification = browser.find_element_by_class_name("alert.alert-success.alert-dismissible")
    notification_text = notification.text.rstrip("\n×'")
    assert notification
    assert notification_text == "Success: You have modified products!"
