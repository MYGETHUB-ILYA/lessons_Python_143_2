from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # Ваш код здесь
# Откройте страницу https://httpbin.org/links/10.
# Найдите все ссылки на странице (тег # <a># ).
    find_elem = driver.find_elements(By.TAG_NAME, "a")
# Проверьте, что количество ссылок равно 9.
    assert len(find_elem) == 9
#    print(f"\nнайдено кол-во ссылок: {len(find_elem)}")

# Проверьте, что все ссылки отображаются на странице.
    for link in find_elem:
        assert link.is_displayed()
# Проверьте, что текст первой ссылки содержит # "1"# . 0 не ссылка!!! а текст.
    first_link = find_elem[0].text
#    print(f"\nтекст первой ссылки: {first_link}")
    assert "1" in first_link

    driver.quit()
