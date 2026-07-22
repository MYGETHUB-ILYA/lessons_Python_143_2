from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org")

    target_link = driver.find_element(By.LINK_TEXT, "HTML form")
    assert target_link.text == "HTML form"

    target_link.click()

    assert "https://httpbin.org/forms/post" in driver.current_url

    driver.back()

    assert "httpbin.org" in driver.current_url
    print('Проверки закончены')

    driver.quit()
