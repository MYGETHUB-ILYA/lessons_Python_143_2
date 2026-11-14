from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import faker

fake = faker.Faker('ru_RU')
first_name = fake.first_name()
last_name = fake.last_name()
zip_code = fake.postcode()
WAIT_TIME = 10


class ShopPage:
    LOGIN_USER = "standard_user"
    PASSWORD_USER = "secret_sauce"
    TOTAL = "$58.29"

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

        input_user = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_USER_LOCATOR)
        )
        input_user.clear()
        input_user.send_keys(self.LOGIN_USER)

        input_password = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_USER_LOCATOR)
        )
        input_password.clear()
        input_password.send_keys(self.PASSWORD_USER)

        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_LOGIN_LOCATOR)
        ).click()
        return self

    def purchase_list(self, total):
        # товары
        self.wait.until(
            EC.element_to_be_clickable(self.PRODUCT_1_LOCATOR)
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(self.PRODUCT_2_LOCATOR)
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(self.PRODUCT_3_LOCATOR)
        ).click()
        # корзина
        self.wait.until(
            EC.element_to_be_clickable(self.CART_CONTAINER_LOCATOR)
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_LOCATOR)
        ).click()

        # форма заказа
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_LOCATOR)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_LOCATOR)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(
            EC.element_to_be_clickable(self.ZIP_CODE_LOCATOR)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(zip_code)

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_LOCATOR)
        ).click()

        # ТОТАЛ
        total_cost = self.driver.find_element(
            *self.TOTAL_LABEL_LOCATOR
        ).text
        print(f"Сумма на сайте: {total_cost}")

        if total in total_cost:
            print(f"Сумма {total_cost} совпадает")
        else:
            print("Сумма не совпадает")

        return self
