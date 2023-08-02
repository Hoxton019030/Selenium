from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()

driver.get('https://www.ptt.cc/bbs/Stock/index.html')
titles =driver.find_elements(By.CLASS_NAME, "title")
print(titles)

for title in titles:
    print(title.text)
# print(driver.page_source)

# driver.close()
