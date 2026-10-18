# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# в браузере Edge (если вы работаете в Windows) или
# Safari (если вы работаете в macOS).
# Заполните форму значениями:
# First name Иван
# first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
# Last name Петров
# last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
# Address Ленина, 55-3
# address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
# Email test@skypro.com
# email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
# Phone number +7985899998787
# phone_num = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
# Zip code *оставить пустым
# zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
# City Москва
# city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
# Country Россия
# country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
# Job position QA
# job_position = driver.find_element(
# By.CSS_SELECTOR, 'input[name="job-position"]')
# Company SkyPro
# company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
# Нажмите кнопку Submit.
# button_submit = driver.find_element(
# By.CSS_SELECTOR, "button.btn-outline-primary")
# Проверьте (assert), что поле Zip code
# подсвечено красным.   #F8D7DA  rgb(248, 215, 218);
# Проверьте (assert ), что остальные поля
# подсвечены зеленым. #D1E7DD  rgb(209, 231, 221);


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Переменные
FIRST_NAME = "Иван"
LAST_NAME = "Петров"
ADDRESS_VAR = "Ленина, 55-3"
EMAIL_VAR = "test@skypro.com"
PHONE_VAR = "+7985899998787"
CITY_VAR = "Москва"
COUNTRY_VAR = "Россия"
JOB_VAR = "QA"
COMPANY_VAR = "SkyPro"


def test_01_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    # first_name
    first_name = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="first-name"]')))
    first_name.clear()
    first_name.send_keys(FIRST_NAME)

    # last_name
    last_name = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="last-name"]')))
    last_name.clear()
    last_name.send_keys(LAST_NAME)

    # address
    address = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="address"]')))
    address.clear()
    address.send_keys(ADDRESS_VAR)
    # email
    email = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="e-mail"]')))
    email.clear()
    email.send_keys(EMAIL_VAR)

    # phone_num
    phone_num = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="phone"]')))
    phone_num.clear()
    phone_num.send_keys(PHONE_VAR)

    # city
    city = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="city"]')))
    city.clear()
    city.send_keys(CITY_VAR)

    # country
    country = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="country"]')))
    country.clear()
    country.send_keys(COUNTRY_VAR)

    # job_position
    job_position = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="job-position"]')))
    job_position.clear()
    job_position.send_keys(JOB_VAR)

    # company
    company = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'input[name="company"]')))
    company.clear()
    company.send_keys(COMPANY_VAR)

    # button_submit
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "button.btn-outline-primary"))).click()

    zip_code = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, '#zip-code')))
    field_color_zip = zip_code.value_of_css_property('background-color')

    assert field_color_zip == 'rgba(248, 215, 218, 1)', "Не красный"
    print("\nРезультаты:")
    print("Поле ZIP красное")

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for name in green_fields:
        field = wait.until(EC.visibility_of_element_located((By.ID, name)))
        field_color = field.value_of_css_property('background-color')
        # print(f"Проверка цвета поля '{name}': {field_color}")
        assert field_color == 'rgba(209, 231, 221, 1)', "Не зеленый"
    print("Все остальные поля зеленые")

    driver.quit()
