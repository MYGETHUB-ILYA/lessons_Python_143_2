from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Ваш код здесь
# Найдите поле ввода с названием custname.
# Введите в него ваше имя.
    driver.find_element(By.NAME, "custname").send_keys("Илья")
# Найдите кнопку Submit и нажмите на нее.
    driver.find_element(By.CSS_SELECTOR, "button").click()
# Проверьте, что после нажатия URL изменился.
    assert "https://httpbin.org/forms/post" in driver.current_url

    driver.quit()
