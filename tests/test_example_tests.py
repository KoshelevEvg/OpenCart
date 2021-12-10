from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import User, Cart
from page_objects import MainPage, UserPage, ProductPage
from page_objects.common import AlertMessage


def test_add_to_wish_list(browser):
    browser.open()
    # Клик по первому элементу в блоке featured
    product_name = MainPage(browser).click_featured_product(1)
    # Клик по кнопке на странице Product
    ProductPage(browser).add_to_wishlist()
    # Клик по ссылке в блоке alert-success локатор Common
    AlertMessage(browser).click_login()
    # Логин с формы авторизации пользователя
    UserPage(browser).login_user(email="test22@mail.ru", password="test")
    # Пеерйти в раздел избранного
    browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)


def test_add_to_cart(browser):
    browser.open()
    # Клик по первому элементу в блоке featured
    product_name = MainPage(browser).click_featured_product(number=1)
    # Клик по кнопке на странице Product
    ProductPage(browser).add_to_cart()
    # Клик по ссылке в блоке alert-success
    AlertMessage(browser).click_to_cart()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)
    # Клик по кнопке Checkout на странице корзины
    browser.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()
    # Логин с формы авторизации пользователя
    UserPage(browser).login_user(email="test22@mail.ru", password='test')
    # Ожидание отображения формы регистрации платежа
    # Alert(browser).accept()
    # browser.find_elements_by_css_selector(User.payment_form.it['css'])

    #WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "payment-new")))
