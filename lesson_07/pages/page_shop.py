from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import faker

fake = faker.Faker('ru_RU')
WAIT_TIME = 10


class ShopPage:
    LOGIN_USER = "standard_user"
    PASSWORD_USER = "secret_sauce"

    # Локаторы для FireFox
    LOGIN_USER_LOCATOR = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_USER_LOCATOR = (By.CSS_SELECTOR, "[data-test='password']")
    BUTTON_LOGIN_LOCATOR = (By.ID, "login-button")
    FIRST_NAME_LOCATOR = (By.ID, "first-name")
    LAST_NAME_LOCATOR = (By.ID, "last-name")
    ZIP_CODE_LOCATOR = (By.ID, "postal-code")
    CONTINUE_LOCATOR = (By.ID, "continue")
    PRODUCT_1_LOCATOR = (By.ID, "add-to-cart-sauce-labs-backpack")
    PRODUCT_2_LOCATOR = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    PRODUCT_3_LOCATOR = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_CONTAINER_LOCATOR = (By.ID, "shopping_cart_container")
    CHECKOUT_LOCATOR = (By.ID, "checkout")
    TOTAL_LABEL_LOCATOR = (By.CSS_SELECTOR, "[data-test='total-label']")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, WAIT_TIME)

    def login_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        user_field = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_USER_LOCATOR))
        user_field.clear()
        user_field.send_keys(self.LOGIN_USER)

        password_field = self.wait.until(
            EC.element_to_be_clickable(
                self.PASSWORD_USER_LOCATOR))
        password_field.clear()
        password_field.send_keys(self.PASSWORD_USER)

        self.wait.until(
            EC.element_to_be_clickable(
                self.BUTTON_LOGIN_LOCATOR)).click()
        return self

    def purchase_list(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_1_LOCATOR)).click()
        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_2_LOCATOR)).click()
        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_3_LOCATOR)).click()
        return self

    def new_form_purchase(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CART_CONTAINER_LOCATOR)).click()
        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_LOCATOR)).click()
        return self

    def client_form(self):
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(
                self.FIRST_NAME_LOCATOR))
        first_name_field.clear()
        first_name_field.send_keys(fake.first_name())

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(
                self.LAST_NAME_LOCATOR))
        last_name_field.clear()
        last_name_field.send_keys(fake.last_name())

        zip_field = self.wait.until(
            EC.element_to_be_clickable(
                self.ZIP_CODE_LOCATOR))
        zip_field.clear()
        zip_field.send_keys(fake.postcode())

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_LOCATOR)).click()
        return self

    def get_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL_LOCATOR)
        ).text
