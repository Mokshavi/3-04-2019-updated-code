import  requests
from bs4 import BeautifulSoup
import  json
import large_automation.config3
import sys

class Scrapy():

    def __init__(self):
        self.head = large_automation.config3.obj.Headers()
        self.cred = large_automation.config3.obj.Credentials()
        self.url1=large_automation.config3.obj.url_store()

    def Login(self):
        #try:
            # print(self.head)
            # print(self.cred)
            # print(self.url)
            with requests.session() as s:
    #             url = "https://rolls-royce.leankit.com/Account/Membership/Authenticate?support=False"

                url_1 = self.url1
                header = json.loads(self.head.replace("'","\""))
                credentials = self.cred

                #print("Credentials are: ", credentials)
                #print("Type of credentials are: ", type(credentials))

                r = s.get(url_1, headers=header)
                #print("Response for GET is: ", r)



                r = s.post(url_1, data=self.cred, headers=header)
                #print("Response for Post is: ", r)
                r = s.get("https://rolls-royce.leankit.com/io/user/me/board/recent?_=1551685125246")
                r=s.get("https://rolls-royce.leankit.c"
                        "om/io/board/106606106?_=1551685125261")
                board_no = ["123457855", "111137067", "106606106", "107600350"]
                for i in board_no:
                    r = s.get("https://rolls-royce.leankit.com/io/board/" + i + "/card?limit=200&id=" + i + "")
                    soup1 = BeautifulSoup(r.content, 'lxml')
                    cards1 = soup1.find("p")
                    cards2 = cards1.text
                    print(cards2)
                    listofcards = []
                    card_Nos = {}
                    card_Nos = json.loads(cards2)
                    # print(card_Nos)
                    asd = card_Nos['cards']
                    print(asd)
                    for i in range(len(asd)):
                        # listofcards=['139017768','126333043','144770704']
                        listofcards.append(card_Nos['cards'][i]['id'])

                    print(listofcards)

                    for i in listofcards:
                        try:
                            r = s.get("https://rolls-royce.leankit.com/io/card/" + i + "?id=" + i + "")
                            soup = BeautifulSoup(r.content, 'lxml')
                            # print(soup.prettify())
                            card = soup.findAll(text=True)
                            # print(len(card))
                            # print(card)
                            # link=card[1]
                            # card_data = card.text
                            if len(card) > 1:
                                card = card[0] + card[len(card) - 1]
                                # print(card)
                                # card_data = card1.text
                            elif len(card) == 1:
                                card = card[0]

                            # print(card_data)
                            card_Details_data = {}
                            card_Details = {}
                            # externalLinks = []

                            card_Details = json.loads(card)
                            # print(card_Details)
                            card_body = soup.find('body')

                            # actualFinish = card_Details["actualFinish"]
                            # actualStart = card_Details['actualStart']
                            # blockedStatus = card_Details['blockedStatus']['isBlocked']
                            # blockedStatus_reason = card_Details['blockedStatus']['reason']
                            # blockedStatus_reason = card_Details['blockedStatus']['date']
                            # board_ID = card_Details['board']['id']
                            # board_Title = card_Details['board']['title']
                            # createdOn = card_Details['createdOn']
                            plannedFinish = card_Details['plannedFinish']
                            externalLinks = card_Details['externalLinks']
                            customId_ConsessionNo = card_Details['customId']['value']
                            if (externalLinks != []):
                                externalLinks = card_Details['externalLinks'][0]['url']
                            elif (externalLinks == None):
                                externalLinks = card_Details['externalLinks'][0]['label']
                            elif (externalLinks == []):
                                externalLinks = soup.findAll(text=True)[1]
                            card_ID = card_Details['id']
                            lane_ID = card_Details['lane']['id']
                            lane_ClassType = card_Details['lane']['laneClassType']
                            lane_title = card_Details['lane']['title']
                            # updatedOn = card_Details['updatedOn']
                            # movedOn = card_Details['movedOn']
                            priority = card_Details['priority']
                            card_size = card_Details['size']
                            card_title = card_Details['title']
                            card_title1 = card_title.split(" ")
                            engieneNo = card_title1[0]
                            engpartNo = str(card_title1[1:])
                            card_type = card_Details['type']['title']
                            if (lane_ClassType == "backlog"):
                                card_Details_data = {"card_title": card_title, "engieneNo": engieneNo, "partNo": engpartNo,
                                                     "customId_ConsessionNo": customId_ConsessionNo,
                                                     "plannedFinish": plannedFinish, "externalLinks": externalLinks,
                                                     "card_ID": card_ID,
                                                     "lane_ID": lane_ID, "lane_ClassType": lane_ClassType,
                                                     "priority": priority,
                                                     "card_size": card_size, "card_type": card_type}
                                print(card_Details_data)
                        except:
                            pass

        # except Exception as e:
        #     print(e)
        #     line = sys.exc_info()[-1].tb_lineno
        #     print(line)



obj1 = Scrapy()
obj1.Login()