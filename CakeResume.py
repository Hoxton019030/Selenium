import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://www.cakeresume.com/jobs/Java?location_list%5B0%5D=Taiwan')

jobTitle = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_jobTitle__Fjzv2')
companyName = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_companyName__QKkj5')
describe = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_description__tNSbN')
jobInfo = driver.find_elements(By.CSS_SELECTOR,
                               '.JobSearchItem_featureSegments__I1Csc > span ')
salary = driver.find_elements(By.CSS_SELECTOR, '.InlineMessage_inlineMessage__I9C_W.InlineMessage_inlineMessageLarge__yeH0A.InlineMessage_inlineMessageDark__rNo_a')

jobInfoString = ""
for i in range(2, len(salary), 5):
    print('i的值現在是',i)
    print(salary[i].text)

print(123)
# for e in jobInfo:
#     print(e.text.strip())
print(321)
time.sleep(1000)
driver.close()
