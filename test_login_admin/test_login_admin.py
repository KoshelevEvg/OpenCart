from locators.LoginAdmin import LoginAdmin


def test_login_admin(browser):
    bro = browser
    send_username = bro.find_element_by_css_selector(LoginAdmin.username)
    send_username.send_keys("admin")
    send_password = bro.find_element_by_css_selector(LoginAdmin.password)
    send_password.send_keys("admin")
    bro.find_element_by_css_selector(LoginAdmin.submit).click()



