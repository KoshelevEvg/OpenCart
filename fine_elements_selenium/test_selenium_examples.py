from selenium.webdriver.support.select import Select

from test_login_admin.locators import MainPage
from selenium.webdriver.common.action_chains import ActionChains


#
def test_element_by_class_name_selector(browser):
    bro = browser
    bro.find_element_by_css_selector(MainPage.promoblock).click()
    bro.find_element_by_class_name("breadcrumb")
#
#
def test_buy_photo(browser):
    br = browser
    br.find_element_by_xpath("//*[@id='content']/div[2]/div[4]/div/div[1]").click()
    select_p = br.find_element_by_css_selector("select[class='form-control']")
    select_photo = Select(select_p)
    select_photo.select_by_value("15")
    qty = br.find_element_by_css_selector("input[name='quantity']")
    qty.clear()
    qty.send_keys("2")
    br.find_element_by_css_selector("button[class = 'btn btn-primary btn-lg btn-block']").click()
    br.find_element_by_css_selector("button[class = 'btn btn-inverse btn-block btn-lg dropdown-toggle']").click()
    # assert br.find_element_by_css_selector("table[class = 'table table-striped']") == True

# def test_element_by_featured_selector(browser):
#     bro = browser
#     bro.find_element_by_css_selector(MainPage.featured_box).click()
#     bro.find_element_by_class_name("breadcrumb")
#
#
# def test_element_by_id(browser):
#     browser.find_element(By.ID, "slideshow0").click()
#     browser.find_element(By.CLASS_NAME, "breadcrumb")
#
#
# def test_element_by_link_text(browser):
#     desktops_link = browser.find_element_by_link_text("Desktops")
#     ActionChains(browser).move_to_element(desktops_link).pause(2).perform()
#     browser.find_element_by_link_text("Show AllDesktops").click()
#     browser.find_element_by_partial_link_text("Your Store").click()


def test_elements_by_css_selector(browser):
    navbar = browser.find_elements_by_xpath("//*[@id='menu']/div[2]/ul/li")
    for item in navbar:
        print(item.get_attribute("class"))
        ActionChains(browser).move_to_element(item).pause(0.5).perform()

# def test_element_by_class_name_selector(parametrize_browser):
#     parametrize_browser.find_element_by_class_name("swiper-viewport").click()
#     parametrize_browser.find_element_by_class_name("breadcrumb")
