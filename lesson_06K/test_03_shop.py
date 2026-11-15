# Создавайте файл test_03_shop.py и добавьте
# в него автотест с шагами:
# Откройте сайт магазина:
# https://www.saucedemo.com/ в FireFox.
# Авторизуйтесь как пользователь standard_user.
# driver.find_element(By.CSS_SELECTOR,
# "[data-test='username']") standard_user
# driver.find_element(By.CSS_SELECTOR,
# "[data-test='password']") secret_sauce
# driver.find_element(By.ID, "login-button") login-button
# !!!! Внимание, появляется
# Всплывающее окно "типа смените пароль"... нужно нажать "Ок"

# Добавьте в корзину товары:
# Sauce Labs Backpack.
# (By.ID, "add-to-cart-sauce-labs-backpack")
# Sauce Labs Bolt T-Shirt.
# (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
# Sauce Labs Onesie.
# (By.ID, "add-to-cart-sauce-labs-onesie")
# Перейдите в корзину.
# (By.ID, "shopping_cart_container")  class= shopping_cart_container
# Нажмите Checkout.
# (driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']"))
# Заполните форму своими данными:
# имя,
# FirstName = driver.find_element(By.ID, "first-name")
# фамилия,
# LastName = driver.find_element(By.ID, "last-name")
# почтовый индекс.
# postal_code = driver.find_element(By.ID, "postal-code")
# Нажмите кнопку Continue.
# button_continue = driver.find_element(By.ID, "continue")
# Прочитайте со страницы итоговую стоимость (Total).
# total = driver.find_element(By.CSS_SELECTOR,
# "[data-test='total-label']") div
# class="summary_total_label" data-test="total-label"
# Закройте браузер.
# driver.quit()
# Проверьте, что итоговая сумма равна $58.29
# total_cost = total.text  # проверить  print(total_cost)
# assert "58.29" in total_cost
# print("right cost")
# проверить

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_USER = "standard_user"
PASSWORD_USER = "secret_sauce"
# "Sauce Labs Backpack"
PRODUCT_1_ID = "add-to-cart-sauce-labs-backpack"
# "Sauce Labs Bolt T-Shirt"
PRODUCT_2_ID = "add-to-cart-sauce-labs-bolt-t-shirt"
# "Sauce Labs Onesie"
PRODUCT_3_ID = "add-to-cart-sauce-labs-onesie"

FIRST_NAME = "Илья"
LAST_NAME = "Трофимов"
ZIP_CODE = "127486"
TOTAL = "$58.29"
WAIT_TIME = 10


def test_03_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, WAIT_TIME)

    user = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "[data-test='username']")))
    user.clear()
    user.send_keys(LOGIN_USER)

    password = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "[data-test='password']")))
    password.clear()
    password.send_keys(PASSWORD_USER)

    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.element_to_be_clickable((By.ID, PRODUCT_1_ID))).click()
    wait.until(EC.element_to_be_clickable((By.ID, PRODUCT_2_ID))).click()
    wait.until(EC.element_to_be_clickable((By.ID, PRODUCT_3_ID))).click()
    wait.until(EC.element_to_be_clickable((
        By.ID, "shopping_cart_container"))).click()
    wait.until(EC.element_to_be_clickable((
        By.ID, "checkout"))).click()

    # -----------------------заполнение------------------------

    first_name = wait.until(EC.element_to_be_clickable((
        By.ID, "first-name")))
    first_name.clear()
    first_name.send_keys(FIRST_NAME)

    last_name = wait.until(EC.element_to_be_clickable((
        By.ID, "last-name")))
    last_name.clear()
    last_name.send_keys(LAST_NAME)

    postal_code = wait.until(EC.element_to_be_clickable((
        By.ID, "postal-code")))
    postal_code.clear()
    postal_code.send_keys(ZIP_CODE)

    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    total_cost = driver.find_element(
        By.CSS_SELECTOR, "[data-test='total-label']").text
    print("\n", total_cost)

    driver.close()
    assert TOTAL in total_cost, "Сумма не совпадает"
    print("Сумма совпадает")

    driver.quit()
