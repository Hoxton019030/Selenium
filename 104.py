import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

from JobDetail import JobDetail

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
url = "https://www.104.com.tw/jobs/search/?https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Java&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001001%2C6001001007%2C6001002000%2C6001001003%2C6001001006%2C6001001002%2C6001001012%2C6001001004%2C6001001005&order=15&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"

driver.get(url)
driver.implicitly_wait(10)
workbook = openpyxl.Workbook()
sheet = workbook.active
headers = ["職務名稱", "公司名稱", "相關描述", "工作簡述", "公司地址", "工作經驗要求", "網址連結"]
sheet.append(headers)

for i in range(113):  # 頁面的interator
    try:

        titles = driver.find_elements(By.CLASS_NAME, "js-job-link")
        companyNames = driver.find_elements(By.CSS_SELECTOR, "ul.b-list-inline.b-clearfix a")
        hrefs = driver.find_elements(By.CLASS_NAME, "js-job-link")
        # 這邊先註解掉，不知道怎麼把薪資抓出來
        # tags = driver.find_elements(By.CLASS_NAME, "b-tag--default")
        # stringTag = ""
        # for tag in tags:
        #     stringTag += tag.text
        # jobInfos = driver.find_elements(By.CLASS_NAME, "job-list-item__info")
        jobInfos = driver.find_elements(By.CSS_SELECTOR, "p.job-list-item__info.b-clearfix.b-content")
        # for jobInfo in jobInfos:
        #     print(jobInfo.text)
        addresses = driver.find_elements(By.CSS_SELECTOR,
                                         "ul.b-list-inline.b-clearfix.job-list-intro.b-content li:first-child")
        experiences = driver.find_elements(By.CSS_SELECTOR,
                                           "ul.b-list-inline.b-clearfix.job-list-intro.b-content li:nth-child(3)")

        job_details_list = []
        for j in range(len(titles)):
            name = ""
            title = titles[j].text
            if "/" in title:
                break
            companyName = companyNames[j].text
            href = hrefs[j].get_attribute('href')
            jobInfo = jobInfos[j].text
            address = addresses[j].text
            experience = experiences[j].text
            job_detail = JobDetail(title, companyName, href, name, jobInfo, address, experience)
            job_details_list.append(job_detail)

        for job in job_details_list:
            rowData = [job.title, job.companyName, job.tags, job.jobInfo, job.address, job.experience, job.href]
            sheet.append(rowData)

        link = driver.find_element(By.CLASS_NAME, "js-next-page")
        link.click()
        time.sleep(2)
        print("目前處理到第", i, "頁")
        workbook.save("test.xlsx")
        print("儲存")

    except Exception as e:

        print(e)
        time.sleep(1)
        continue

print("儲存")
workbook.close()

# for some in hrefs:
#     print(some.get_dom_attribute('href'))
# print(titles)
# time.sleep(10)
# a = JobDetail()
# for title in titles:
#     print(title.text)
# for companyName in companyNameList:
#     print(companyName.text)
# for tag in tags:
#     print(tag.text)

# print(driver.page_source)
# 取得上一頁的文章標題


# time.sleep(10)
# driver.close()
