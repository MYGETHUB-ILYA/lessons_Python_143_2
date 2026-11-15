import pytest
from selenium import webdriver
from pages.page_shop import ShopPage

URL = "https://www.saucedemo.com/"
TOTAL = "$58.29"
# TOTAL = "$18.29" # контроль падения теста


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    page = ShopPage(driver, URL)
    (page
     .login_page()
     .purchase_list()
     .new_form_purchase()
     .client_form())

    total_cost = page.get_total()
    assert TOTAL in total_cost, f"Cумма {TOTAL}, не совпадает: {total_cost}"
