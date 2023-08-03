import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.send_keys('武嶺')
search.send_keys(Keys.ENTER)

time.sleep(100)
