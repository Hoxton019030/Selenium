from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_locationsq = "/usr/bin/chromium"
driver = webdriver.Chrome()

driver.get('https://python.org')
driver.save_screenshot("screenshot.png")

driver.close()
print("成功")

url = "https://www.104.com.tw/job/ajax/content/4sq6c"

response =requests.get(url)
print(response.text)
