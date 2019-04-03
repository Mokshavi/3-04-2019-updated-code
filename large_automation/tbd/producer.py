import pika
from large_automation import config
import json
class rabbitmouse:
    def rbproducer(self,dataobject):
        object = config()
        asd = object.dataobject()
        print(len(asd))
        for asd1 in asd:
            asd2 = json.dumps(asd1.__dict__)
            connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            channel = connection.channel()
            # channel.exchange_declare(exchange="",exchange_type="")
            channel.basic_publish(exchange='', routing_key='hello', body=asd2)
            print("[x] sent hello world")
            connection.close()











