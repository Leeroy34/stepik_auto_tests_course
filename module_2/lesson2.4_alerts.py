from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
# нажимаем кнопку
browser.find_element(By.TAG_NAME, 'button').click()
# принимаем подтверждение
confirm = browser.switch_to.alert
confirm.accept()
x = browser.find_element(By.ID, 'input_value').text
summ = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(summ)
browser.find_element(By.TAG_NAME, "button").click()
time.sleep(30)
