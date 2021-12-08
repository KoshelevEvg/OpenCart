from locators import LoginAdmin, ProductPage


def test_add_position(browser):
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
    browser.find_element_by_css_selector(ProductPage.add_position).click()
    browser.find_element_by_css_selector(ProductPage.product_name).send_keys("Test product")
    browser.find_element_by_css_selector(ProductPage.meta_tag).send_keys("Test meta tag product")
    form_horizonts = browser.find_elements_by_css_selector("ul.nav.nav-tabs > li")
    for form_horizont in form_horizonts:
        if form_horizont.text == "Data":
            form_horizont.click()
            break
    browser.find_element_by_css_selector(ProductPage.model).send_keys("Product 15")
    browser.find_element_by_css_selector(ProductPage.save).click()
    notification = browser.find_element_by_class_name("alert.alert-success.alert-dismissible")
    notification_text = notification.text.rstrip("\n×'")
    assert notification
    assert notification_text == "Success: You have modified products!"
    # browser.quit()
