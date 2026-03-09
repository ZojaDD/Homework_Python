import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from pages.AutoPage import AutoPage
from pages.MainShopPage import MainShopPage
from pages.CardPage import CardPage
from pages.ResultPage import ResultPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()  # Максимизируем окно браузера
    driver.set_page_load_timeout(10)  # Ожидание загрузки страницы
    yield driver
    driver.quit()  # Закрыть браузер после завершения тестов


def test_shopping_cart(driver):
    auto_page = AutoPage(driver)
    auto_page.open()
    auto_page.authorization()

    main_shop_page = MainShopPage(driver)
    main_shop_page.shop_page()
    main_shop_page.transfer_cart()

    card_page = CardPage(driver)
    card_page.fill_form()
    card_page.click_continue()

    result_page = ResultPage(driver)
    result_page.summary()

    result_value = result_page.summary()
    assert result_value == 58.29
