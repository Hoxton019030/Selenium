import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://www.dcard.tw/f/cycu')
time.sleep(100)

# for i in range(10):
#     time.sleep(2)
#     link = driver.find_element(By.CLASS_NAME, "js-next-page")
#     link.click()


# titles = driver.find_elements(By.CLASS_NAME, "js-job-link")
# jobInfos = driver.find_elements(By.CSS_SELECTOR, "p.job-list-item__info.b-clearfix.b-content")
# experiences = driver.find_elements(By.CSS_SELECTOR,
#                                    "ul.b-list-inline.b-clearfix.job-list-intro.b-content li:nth-child(3)")
# keyword = driver.find_element(By.ID, "main-content")
# hrefs = driver.find_elements(By.CLASS_NAME, "js-job-link")

# print(keyword.text)
# driver.close()
