from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/redirect_accept.html"


browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, 'button').click()
# переключаемся на новое окно. Сначала задаем нужное
new_window = browser.window_handles[1]
# переключаемся на выбранное окно
browser.switch_to.window(new_window)
x = browser.find_element(By.ID, 'input_value').text
summ = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(summ)
browser.find_element(By.TAG_NAME, "button").click()
time.sleep(30)
