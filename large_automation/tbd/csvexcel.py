import csv
from large_automation.WebScrapy import Scrapy
class csvexcel:
    def latestvalues(self,carddata):
        #results = []
        with open('C:\\Users\\1023816\\Downloads\\modified-code-master\\csvfile\\new.csv') as carddata:
            reader = csv.reader('consessionnum')
            #for row in reader:
            print(reader)


    def writingdata(self,carddata):
        myData = [carddata]
        print(carddata)
        myFile = open('C:\\Users\\1023816\\Downloads\\modified-code-master\\csvfile\\new.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)

        print("Writing complete")








