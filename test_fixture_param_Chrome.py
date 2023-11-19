# Обучение использованию параметризации 
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
# Тест запустится на каждой из страниц
@pytest.mark.parametrize('linker', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])

def test_guest_should_see_login_link(browser, linker):
    link = linker
    #print("link = ", link)
    browser.get(link)
    time.sleep(2)

    # Ищем кнопку "Войти"
    button = browser.find_element(By.ID, "ember33")
    # Нажали "Войти"
    button.click()

    time.sleep(1)

    # Заполняем поле с логином
    element = browser.find_element(By.ID, "id_login_email")
    element.send_keys("ju-ilyina@yandex.ru")

    # Заполняем поле с паролем
    element = browser.find_element(By.ID, "id_login_password")
    element.send_keys("98765432") # не настоящий пароль

    # Ищем кнопку "Войти"
    button_enter = browser.find_element(By.XPATH, ".//*[@type='submit']")
    button_enter.click()

    time.sleep(3)

    # Считаем число для подстановки в форму
    answer = math.log(int(time.time()))

    # Вносим подсчитанное число в форму
    element = browser.find_element(By.XPATH, ".//*[@class='ember-text-area ember-view textarea string-quiz__textarea']")
    element.send_keys(answer)

    # Отправляем результат нажатием кнопки "Войти"
    button_enter = browser.find_element(By.XPATH, ".//*[@class='submit-submission']")
    button_enter.click()

    # ждем загрузки страницы, забираем результат
    time.sleep(2)
    result = browser.find_element(By.XPATH, ".//*[@class='smart-hints__hint']")
    res = result.text
    print("res", res)
    
