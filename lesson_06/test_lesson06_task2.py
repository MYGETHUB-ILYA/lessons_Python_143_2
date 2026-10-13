from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# добавлены, часто падал тест
from selenium.webdriver.chrome.options import Options
import time


def wait_for_syte_answer():  # добавлен, часто падал тест
    time.sleep(5)


def test_session_storage_auth():
    options = Options()                         # добавлен, часто падал тест
    options.page_load_strategy = 'eager'        # добавлен, часто падал тест
    driver = webdriver.Chrome(options=options)  # добавлен, часто падал тест
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gitflic.ru/")
    wait = WebDriverWait(driver, 40)
    driver.delete_all_cookies()

    driver.find_element(By.CSS_SELECTOR, '[href="/auth/login"]').click()
    wait_for_syte_answer()

    input_login = driver.find_element(By.ID, "email")
    input_login.clear()
    input_login.send_keys("trofimov.world@yandex.ru")
    wait_for_syte_answer()
    input_password = driver.find_element(By.ID, "passwordBasic")
    input_password.clear()
    input_password.send_keys("A1S2D3F4q1w2e3r4*g")
    wait_for_syte_answer()
    submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
    submit_button.click()

    wait_for_syte_answer()

    # ПРОВЕРЯЕМ НА ЭКРАН С КУКИ! СОГЛАСИЕ С НИМИ через try:
    try:
        cookies_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".cookiesBtn"))
        )
        cookies_btn.click()
        print("Куки приняты")
    except NoSuchElementException:
        print("Окно с куки не появилось — пропускаем")

    driver.find_element(
        By.CSS_SELECTOR, ".text-dark.profile-page__profile-name"
    ).click()

    first_url = driver.current_url
    print(first_url)

    wait_for_syte_answer()

    # ВЫХОД
    driver.find_element(
        By.CSS_SELECTOR,
        "button.gf-dropdown__toggle.btn.btn-link.text-muted.pl-0"
    ).click()
    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "gf-icon-logout"))
    ).click()

    wait_for_syte_answer()
    driver.refresh()
    driver.delete_all_cookies()
    wait_for_syte_answer()

    # Второй    https: // gitflic.ru / user / ilya_trofimov
    driver.find_element(By.CSS_SELECTOR, '[href="/auth/login"]').click()

    input_login = driver.find_element(By.ID, "email")
    input_login.clear()
    input_login.send_keys("trofimov7375@yandex.ru")
    wait_for_syte_answer()
    input_password = driver.find_element(By.ID, "passwordBasic")
    input_password.clear()
    input_password.send_keys("MyBigParole2026")
    wait_for_syte_answer()
    submit_button = driver.find_element(By.CLASS_NAME, 'btn-success')
    submit_button.click()

    try:
        cookies_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".cookiesBtn"))
        )
        cookies_btn.click()
        print("Куки приняты")
    except NoSuchElementException:
        print("Окно с куки не появилось — пропускаем")
    wait_for_syte_answer()

    driver.find_element(
        By.CSS_SELECTOR, ".text-dark.profile-page__profile-name"
    ).click()

    second_url = driver.current_url
    print(second_url)

    assert first_url != second_url, \
        f"URL одинаковы! {first_url} == {second_url}"
    print("Проверка пройдена: URL разные")

    driver.quit()
