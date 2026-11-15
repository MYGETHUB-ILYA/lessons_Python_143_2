import pytest
from selenium import webdriver
from pages.page_calc import CalcPage

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
WAIT_TIME_VAR = 45
NUMBER_TEST = 15
# NUMBER_TEST = 14 # для контроля теста
NUMBER_TEST_CONTR = 15


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
     .result_calculation())

    fact_result = page.assert_calculation(NUMBER_TEST)

    print(
        f"Результат {
            'совпадает' if fact_result == str(NUMBER_TEST)
            else 'не совпадает'}")

    assert fact_result == str(NUMBER_TEST), (
        f"результат не '{NUMBER_TEST}', а '{fact_result}'"
    )
