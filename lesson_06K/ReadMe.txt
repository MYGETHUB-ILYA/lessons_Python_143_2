Это папка с контрольной по автоматизации тестов.


Критерии оценки
Работа будет оценена по следующим критериям
01. Создана ветка lesson6K (выполнено)
02. Создана папка lesson_06K (выполнено)
03. Отчет линтера не содержит ошибок (errors) и предупреждений (warnings).
04. Файл для автотеста на «Форму» имеет имя test_01_form.py, содержит функцию test_.... и использует явные ожидания (WebDriverWait) и нет sleep().
05. Автотест на «Форму» выполняется успешно и соответствует сценарию из ТЗ.
06. Файл для автотеста на «Калькулятор» имеет имя test_02_calc.py, содержит функцию test_... и использует явные ожидания (WebDriverWait) и нет sleep()..
07. Автотест на «Калькулятор» выполняется успешно и соответствует сценарию из ТЗ.
08. Файл для автотеста на «Покупку» имеет имя test_03_shop.py, содержит функцию test_.... и использует явные ожидания (WebDriverWait) и нет sleep().
09. Автотест на «Покупку» выполняется успешно и соответствует сценарию из ТЗ.
10. Pull Request создан из ветки lesson6K в master/main, ссылка приложена в формате https://github.com/.../pull/N.


---test_01_form.py------------------------------------------------------------------------------
Задание 1. Написать автотесты
Создайте файл test_01_form.py и добавьте в него автотест с шагами:
Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
в браузере Edge (если вы работаете в Windows) или Safari (если вы работаете в macOS).
Заполните форму значениями:
First name Иван                 # first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
Last name Петров                # last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
Address Ленина, 55-3            # address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
Email test@skypro.com           # email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
Phone number +7985899998787     # phone_num = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
Zip code *оставить пустым       # zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
City Москва                     # city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
Country Россия                  # country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
Job position QA                 # job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
Company SkyPro                  # company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
Нажмите кнопку Submit.          # button_submit = driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary")
Проверьте (assert), что поле Zip code подсвечено красным.   #F8D7DA  rgba(248, 215, 218, 1);
Проверьте (assert ), что остальные поля подсвечены зеленым. #D1E7DD  rgba(209, 231, 221, 1);

---test_02_calc.py------------------------------------------------------------------------------
2) Калькулятор
Создайте файл test_02_calc.py и добавьте в него автотест с шагами:
Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
В поле ввода по локатору #delay введите значение 45.
# number_wait =  driver.find_element(By.ID, "delay") или (By.CSS_SELECTOR, "#delay") #в начале отчистить от 5
Нажмите на кнопки:  (как вариант //div[@id='calculator']//span[text()='7'])
7                   # Кнопка "7" driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']")
+                   # Кнопка "+" driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']")
8                   # Кнопка "8" driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']")
=                   # Кнопка "=" driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")

Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
# result = driver.find_element(By.CSS_SELECTOR, "top.screen")  == 15
# Не забудь сброс reset = driver.find_element(By.CSS_SELECTOR, "clear.btn.btn-outline-danger")

---test_03_shop.py------------------------------------------------------------------------------
3) Покупка
Создавайте файл test_03_shop.py и добавьте в него автотест с шагами:

Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
Авторизуйтесь как пользователь standard_user.
                                                        # driver.find_element(By.CSS_SELECTOR, "[data-test='username']") standard_user
                                                        # driver.find_element(By.CSS_SELECTOR, "[data-test='password']") secret_sauce
                                                        # driver.find_element(By.ID, "login-button") login-button
                                                        #!!!! Внимание, появляется Всплывающее окно "типа смените пароль"... нужно нажать "Ок"

Добавьте в корзину товары:
Sauce Labs Backpack.                                    # (By.ID, "add-to-cart-sauce-labs-backpack")
Sauce Labs Bolt T-Shirt.                                # (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
Sauce Labs Onesie.                                      # (By.ID, "add-to-cart-sauce-labs-onesie")
Перейдите в корзину.                                    # (By.ID, "shopping_cart_container")  class= shopping_cart_container
Нажмите Checkout.                                       # (driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']"))
Заполните форму своими данными:
имя,                                                    # FirstName = driver.find_element(By.ID, "first-name")
фамилия,                                                # LastName = driver.find_element(By.ID, "last-name")
почтовый индекс.                                        # postal_code = driver.find_element(By.ID, "postal-code")
Нажмите кнопку Continue.                                # button_continue = driver.find_element(By.ID, "continue")
Прочитайте со страницы итоговую стоимость (Total).      # total = driver.find_element(By.CSS_SELECTOR,"[data-test='total-label']") div class="summary_total_label" data-test="total-label"
Закройте браузер.                                       # driver.quit()
Проверьте, что итоговая сумма равна $58.29              # total_cost = total.text  # проверить  print(total_cost)
                                                        # assert "58.29" in total_cost
                                                        # print("right cost")      # проверить


---------------------------------------------------------------------------------