# 1 аккаунт
# trofimov.world@yandex.ru
# A1S2D3F4q1w2e3r4*g

# 2 аккаунт
# trofimov7375@yandex.ru
# MyBigParole2026


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SESSION_VALUE_1 = "MDVmODE0ODUtYmY0My00MGFiLThlMWUtMWEyOWRjZjU2OThk"
SESSION_VALUE_2 = "ZjEwMmZiZmUtYWViMC00ZjI5LTg1NjAtMTRhNTExYmU3NmZj"
COOKIES_ACCEPTED = "true"
BASE_URL = "https://gitflic.ru/"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 50)

    # Cookies 1-го аккаунта

    driver.add_cookie({
        "name": "SESSION",
        "value": SESSION_VALUE_1
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": COOKIES_ACCEPTED
    })

    driver.refresh()

    profile_element = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "header-username")
        )
    )
    profile_element.click()

    first_url = driver.current_url
    print(first_url)

    driver.get(BASE_URL)
    driver.delete_all_cookies()

    # Cookies 2-го аккаунта
    driver.add_cookie({
        "name": "SESSION",
        "value": SESSION_VALUE_2
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": COOKIES_ACCEPTED
    })
    driver.refresh()

    profile_element = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "header-username")
        )
    )

    profile_element.click()

    second_url = driver.current_url
    print(second_url)

    assert first_url != second_url, \
        f"URL одинаковы! {first_url} == {second_url}"
    print("Проверка пройдена: URL разные")

    driver.refresh()
    driver.delete_all_cookies()

    driver.quit()
