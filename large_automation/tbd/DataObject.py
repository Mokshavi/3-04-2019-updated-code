from large_automation import WebScrapy
from large_automation.carddetails import Service
class DataObject:

 def dataobjectcreation(self,carddata):
     """card_Details_data = {"card_title": card_title, "engieneNo": engieneNo, "partNo": engpartNo,
                           "customId_ConsessionNo": customId_ConsessionNo,
                           "plannedFinish": plannedFinish, "externalLinks": externalLinks,
                           "card_ID": card_ID,
                           "lane_ID": lane_ID, "lane_ClassType": lane_ClassType,
                           "priority": priority,
                           "card_size": card_size, "card_type": card_type}"""
     # print(carddata)
     s1 = Service("card_title", "engieneNo", "engpartNo", "customId_ConsessionNo", "plannedFinish", "externalLinks","card_ID","card_size","lane_ID", "lane_ClassType", "priority", "card_type")
     s1.set_card_title(carddata['card_title'])
     s1.set_engieneNo(carddata['engieneNo'])
     s1.set_engpartNo(carddata['partNo'])
     #s1.set_engieneNo("engieneNo")
     # s1.set_engpartNo("engpartNo")
     s1.set_customId_ConsessionNo(carddata["customId_ConsessionNo"])
     s1.set_plannedFinish(carddata["plannedFinish"])
     s1.set_externalLinks(carddata["externalLinks"])
     s1.set_card_ID(carddata["card_ID"])
     s1.set_card_size(carddata["card_size"])
     s1.set_lane_ID(carddata["lane_ID"])
     s1.set_lane_ClassType(carddata["lane_ClassType"])
     s1.set_priority(carddata["priority"])
     s1.set_card_type(carddata["card_type"])
     #return s1









