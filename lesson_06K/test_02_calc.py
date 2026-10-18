# Создайте файл test_02_calc.py и добавьте в него
# автотест с шагами:
# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# в Google Chrome.
# В поле ввода по локатору (#delay) введите значение 45.
# number_wait =  driver.find_element(By.ID, "delay") или
# (By.CSS_SELECTOR, "#delay") #в начале отчистить от 5
# Нажмите на кнопки:
# (как вариант //div[@id='calculator']//span[text()='7'])
# Кнопка "7" driver.find_element(
# By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']")
# Кнопка "+" driver.find_element(# By.XPATH,
# "//span[@class='operator btn btn-outline-success' and text()='+']")
# Кнопка "8" driver.find_element(By.XPATH,
# "//span[@class='btn btn-outline-primary' and text()='8']")
# Кнопка "=" driver.find_element(By.XPATH,
# "//span[@class='btn btn-outline-warning' and text()='=']")

# Проверьте (assert), что в окне отобразится
# результат 15 через 45 секунд.
# result = driver.find_element(
# By.CSS_SELECTOR, "top.screen")  == 15
# Не забыть !!! сброс reset = driver.find_element(
# By.CSS_SELECTOR, "clear.btn.btn-outline-danger")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WAIT_TIME = 10
WAIT_TIME_NEW = 46


def test_02_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, WAIT_TIME)

    number_wait = wait.until(EC.element_to_be_clickable((
        By.ID, "delay")))
    number_wait.clear()
    number_wait.send_keys("45")

    # сброс, если вдруг есть что-то
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, ".clear.btn.btn-outline-danger"))).click()
    # 7
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span[@class='btn btn-outline-primary' and text()='7']"))).click()
    # +
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span[@class='operator btn btn-outline-success' and text()='+']"))
    ).click()
    # 8
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span[@class='btn btn-outline-primary' and text()='8']"))
    ).click()
    # =
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span[@class='btn btn-outline-warning' and text()='=']"))
    ).click()

    wait = WebDriverWait(driver, WAIT_TIME_NEW)

    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15"))
    result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert result_element.text == "15", "Не верно"
    print("\nВсё верно. Результат 15")

    driver.quit()
