import pytest
from selenium import webdriver
from pages.page_calc import CalcPage

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
WAIT_TIME_VAR = 45


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calc(driver):
    page = CalcPage(driver, URL)
    (page
        .open_page()
        .input_number_wait(WAIT_TIME_VAR)
        .result_calculation()
        .assert_calculation())
