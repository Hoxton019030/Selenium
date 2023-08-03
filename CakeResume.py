import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
workbook = openpyxl.Workbook()
sheet = workbook.active
headers = ["職務名稱", "公司名稱", "相關描述", "工作簡述", "公司地址", "薪資", "網址連結"]
sheet.append(headers)
for i in range(0, 36):
    print("第" + str(i + 1) + "頁")
    url = 'https://www.cakeresume.com/jobs/JAVA?location_list%5B0%5D=%E5%8F%B0%E5%8C%97%E5%B8%82%2C%20%E5%8F%B0%E7%81%A3&location_list%5B1%5D=%E5%8F%B0%E7%81%A3%E5%8F%B0%E5%8C%97%E5%B8%82&location_list%5B2%5D=%E6%96%B0%E5%8C%97%E5%B8%82%2C%20%E5%8F%B0%E7%81%A&page=' + str(
        i + 1)
    driver.get(url)
    time.sleep(2)

    jobTitle = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_jobTitle__Fjzv2')
    link = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_jobTitle__Fjzv2')
    companyName = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_companyName__QKkj5')
    describe = driver.find_elements(By.CLASS_NAME, 'JobSearchItem_description__tNSbN')
    address = driver.find_elements(By.CSS_SELECTOR,
                                   '.JobSearchItem_featureSegments__I1Csc > span ')
    salary = driver.find_elements(By.CSS_SELECTOR,
                                  '.InlineMessage_inlineMessage__I9C_W.InlineMessage_inlineMessageLarge__yeH0A.InlineMessage_inlineMessageDark__rNo_a')

    # for e in link:
    #     print(e.get_attribute('href'))

    # for j in range(2, len(salary), 5):
    #     print('i的值現在是', j)
    #     print(salary[j].text)

    for j in range(len(jobTitle)):
        try:
            print(jobTitle[j].text)
            test = [jobTitle[j].text,
                    companyName[j].text,
                    describe[j].text,
                    address[j].text,
                    salary[j * 5 + 2].text,
                    link[j].get_attribute('href')
                    ]
            sheet.append(test)
        except Exception as e:
            print("An error occurred:", e)
            continue

    workbook.save("cakeResume.xlsx")

print("開始")
print("結束")
time.sleep(1)
driver.close()
