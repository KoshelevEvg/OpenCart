from selenium.webdriver import ActionChains

from locators import LoginAdmin


def test_categories(browser, request):
    # url = ""
    # browser.get("".join([request.config.getoption("--url"), url]))
    browser.find_element_by_css_selector(LoginAdmin.username).send_keys("admin")
    browser.find_element_by_css_selector(LoginAdmin.password).send_keys("admin")
    browser.find_element_by_css_selector(LoginAdmin.submit).click()
    browser.find_element_by_css_selector("button.close").click()
    browser.find_element_by_css_selector("#menu-catalog").click()
    catalog_elements = browser.find_elements_by_css_selector("li")
    for catalog_element in catalog_elements:
        if catalog_element.text == "Products":
            catalog_element.click()
            break
    browser.find_element_by_xpath("//*[@id='form-product']/div/table/tbody/tr[8]/td[8]/a/i").click()
    browser.find_element_by_css_selector("input[placeholder='Product Name']").send_keys("Test123")
    browser.find_element_by_css_selector("input[placeholder='Meta Tag Title']").clear()
    browser.find_element_by_css_selector("input[placeholder='Meta Tag Title']").send_keys("Test123")
    browser.find_element_by_class_name("fa.fa-save").click()
    notification = browser.find_element_by_class_name("alert.alert-success.alert-dismissible")
    notification_text = notification.text.rstrip("\n×'")
    assert notification
    assert notification_text == "Success: You have modified products!"
    # browser.quit()


