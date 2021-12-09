from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Main, Product, Common, User


def test_add_to_wish_list(browser):
    browser.open()
    # Клик по первому элементу в блоке featured
    feature_product = browser.find_elements_by_css_selector(Main.featured.products['css'])[0]
    product_name = feature_product.find_element_by_css_selector(Main.featured.names['css']).text
    feature_product.click()
    # Клик по кнопке на странице ProductzZ
    browser.find_element_by_css_selector(Product.add_to_wishlist['css']).click()
    # Клик по ссылке в блоке alert-success локатор Common
    browser.find_element_by_css_selector(Common.alert_mes.success.login['css']).click()
    # Логин с формы авторизации пользователя
    browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys("test22@mail.ru")
    browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys("test")
    browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()
    # Пеерйти в раздел избранного
    browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)


def test_add_to_cart(browser):
    browser.open()
    # Клик по первому элементу в блоке featured
    feature_product = browser.find_elements_by_css_selector(Main.featured.products['css'])[0]
    product_name = feature_product.find_element_by_css_selector(Main.featured.names).text
    feature_product.click()
    # Клик по кнопке на странице Product
    browser.find_element_by_css_selector(Product.add_to_cart['css']).click()
    # Клик по ссылке в блоке alert-success
    browser.find_element_by_css_selector(Common.alert_mes.success.to_cart['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)
    # Клик по кнопке Checkout на странице корзины
    browser.find_element_by_css_selector(Common.alert_mes.success.to_cart['css']).click()
    # Логин с формы авторизации пользователя
    browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys("test")
    browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys("test22@mail.ru")
    browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()
    # Ожидание отображения формы регистрации платежа
    browser.find_elements_by_css_selector(User.payment_form.it['css'])

    #WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "payment-new")))
