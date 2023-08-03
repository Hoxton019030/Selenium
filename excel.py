import openpyxl
from openpyxl.styles import Font
import os

workbook = openpyxl.Workbook()

ws = workbook.active
ws.title = "QQ";
headers = ["職務名稱", "公司名稱", "相關標籤", "工作簡述", "公司地址", "工作經驗要求", "網址連結"]
ws.append(headers)
# sheet = workbook.create_sheet("工作資料", 0)
# print(sheet.append(1))

workbook.save("Done.xlsx")
# workbook.save("test.xlsx")
# workbook.close()
