from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")



# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

xpath_testing = "//button[text()='Book']"
button = browser.find_element(By.XPATH, xpath_testing)
button.click()

num_1 = browser.find_element(By.ID, "input_value")

res = calc(int(num_1.text))
res = str(res)

element = browser.find_element(By.ID, "answer")
element.send_keys(res)

# Отправляем заполненную форму
xpath_testing = "//button[text()='Submit']"
button = browser.find_element(By.XPATH, xpath_testing)
button.click()

time.sleep(10)

