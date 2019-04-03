from xlwt import Workbook
#from practicing.rabbitmouse import rabbitmouse
from large_automation import WebScrapy
class excel:
    wb = Workbook()
    # rb = rabbitmouse()
    sc = WebScrapy()
    mini = sc.details()
    # def insertion(self):
    leankit = wb.add_sheet('leankit')
    leankit.write(0, 0, 'Sno')
    leankit.write(0, 1, 'card_title')
    leankit.write(0, 2, 'engieneNo')
    leankit.write(0, 3, 'engpartNo')
    leankit.write(0, 4, 'customId_ConsessionNo')
    leankit.write(0, 5, "plannedFinish")
    leankit.write(0, 6, "externalLinks")
    leankit.write(0, 7, "lane_ID")
    leankit.write(0, 8, "lane_ClassType")
    leankit.write(0, 9, "priority")
    leankit.write(0, 10, "card_type")
    # add_sheet is used to create sheet.

    # leankit.write(0, 1, 'review')
    the = leankit.write(0, 1, 'card_title')
    for i2 in mini:
        e = i2.get_card_title
        print(e)
    wb.save(' xlwt card.xls')

