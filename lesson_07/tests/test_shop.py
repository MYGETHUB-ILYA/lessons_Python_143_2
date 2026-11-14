import pytest
from selenium import webdriver
from pages.page_shop import ShopPage

URL = "https://www.saucedemo.com/"
TOTAL = "$58.29"


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    page = ShopPage(driver, URL)
    (page
        .login_page()
        .purchase_list(TOTAL))
