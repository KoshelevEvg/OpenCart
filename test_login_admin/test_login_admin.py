import pytest

from locators import LoginAdmin


@pytest.fixture(scope="session")
def open_login_page(browser, request):
    url = ""
    return browser.get("".join([request.config.getoption("--url"), url]))


# @pytest.fixture
# def login_page(browser):
#     return LoginAdmin(browser)


@pytest.fixture(scope="function")
def test_login_admin(browser):
    bro = browser
    send_username = bro.find_element_by_css_selector(LoginAdmin.username).send_keys("admin")
    send_password = bro.find_element_by_css_selector(LoginAdmin.password).send_keys("admin")
    bro.find_element_by_css_selector(LoginAdmin.submit).click()


# @pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class Test:

    @pytest.mark.usefixtures("test_login_admin")
    def test_login(self, browser):
        print(browser.current_url)
        assert "dashboard" in browser.current_url


