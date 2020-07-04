import asyncio
from nats.aio.client import Client as NATS
import pymongo
import json

def insert(data= '{"Nombre": "Jimmixxx Dalton","Departamento": "Chiquimula","Edad": 66,"Forma de contagio": "Comunitario","Estado": "Recuperado"  }'):

    client = pymongo.MongoClient("mongodb://0.0.0.0", port=27017)
    db = client.DB_SP1_P2_201314716
    dataJson = json.loads(data)
    db.Covid.insert_one({"Nombre":dataJson['Nombre'], "Departamento": dataJson['Departamento'], "Edad":dataJson['Edad'], "Forma de contagio" : dataJson['Forma de contagio'], "Estado": dataJson['Estado']}).inserted_id


async def run(loop):
    nc = NATS()
    await nc.connect("nats://0.0.0.0:4222", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        insert(data)
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    await nc.subscribe("foo", cb=message_handler)
    await nc.flush()





if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()