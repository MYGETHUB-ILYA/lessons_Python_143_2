from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    # Локаторы элементов калькулятора
    WAIT_BOX_VAR = (By.ID, "delay")
    CLEAN_BUTTON = (By.CSS_SELECTOR, ".clear.btn.btn-outline-danger")
    BUTTON_7 = (
        By.XPATH,
        "//span[@class='btn btn-outline-primary' and text()='7']")
    BUTTON_8 = (
        By.XPATH,
        "//span[@class='btn btn-outline-primary' and text()='8']")
    BUTTON_PLUS = (
        By.XPATH,
        "//span[@class='operator btn btn-outline-success' and text()='+']")
    BUTTON_EQUALS = (
        By.XPATH,
        "//span[@class='btn btn-outline-warning' and text()='=']")
    RESULT_BOX = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.delay_time = 10

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self

    def input_number_wait(self, wait_time):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.WAIT_BOX_VAR)
        )
        input_field.clear()
        input_field.send_keys(str(wait_time))

        self.delay_time = int(wait_time)
        return self

    def result_calculation(self):
        self.wait.until(EC.element_to_be_clickable(self.CLEAN_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_7)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLUS)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_8)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_EQUALS)).click()
        return self

    def assert_calculation(self):
        dynamic_wait = WebDriverWait(self.driver, self.delay_time + 10)
        result_present = dynamic_wait.until(
            EC.text_to_be_present_in_element(self.RESULT_BOX, "15")
        )

        assert result_present is True, (
            f"Ожидался результат '15', за {self.delay_time + 5} секунд"
        )
        print("Ок. Результат 15")
        return self
