from large_automation.Web_scrapy_6 import Web_Scrapy
import os
obj1 = Web_Scrapy()

# card_details = obj1.executor()
# print(card_details)
#csvFile = open('Data_Validation.csv','w')


if not os.path.exists('Data_Validation.csv'):
    with open('Data_Validation.csv','w') as csv_file:
        print("data file created")
