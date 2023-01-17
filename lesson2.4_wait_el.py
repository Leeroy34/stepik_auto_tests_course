from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# button = WebDriverWait(browser, 5).until(
#     EC.element_to_be_clickable((By.ID, "verify"))
# )
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
    (By.ID, "price"), "100"))

book = browser.find_element(By.ID, "book")
book.click()
x = browser.find_element(By.ID, 'input_value').text
summ = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(summ)
browser.find_element(By.ID, "solve").click()
time.sleep(30)
