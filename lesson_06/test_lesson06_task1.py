# Шаги
# Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
# Найдите и нажмите на кнопку Start.
# Дождитесь появления текста Hello World!
# Сделайте скриншот страницы.
# Проверьте, что появившийся текст равен Hello World!
# Код для выполнения:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # добавлен, падал тест


def test_dynamic_loading():
    options = Options()                          # часто падал тест
    options.page_load_strategy = 'eager'         # часто падал тест

    driver = webdriver.Chrome(options=options)   # часто падал тест
    driver.maximize_window()
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"   $(['#Start']) - 1
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!" id="finish"
    text_hello = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'finish'))
    )
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("lesson_06/screenshots/full_screen_HW_001.png")
    # Проверяем, что текст в нём совпадает с нужным значением
    assert text_hello.text.strip() == 'Hello World!'

    driver.quit()
