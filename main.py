from selenium import webdriver
from  selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()

driver.get('https://python.org')
driver.save_screenshot("screenshot.png")

driver.close()
print("成功")