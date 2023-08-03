from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()

driver.get('https://www.ptt.cc/bbs/Stock/index.html')
titles = driver.find_elements(By.CLASS_NAME, "title")
print(titles)

for title in titles:
    print(title.text)
# print(driver.page_source)
# 取得上一頁的文章標題

link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click()
# driver.close()
