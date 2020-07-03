import asyncio
from nats.aio.client import Client as NATS
import pymongo

client = pymongo.MongoClient("url", 27017)


async def run(loop):
    nc = NATS()
    await nc.connect("url", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()

        db = client['DB_SP1_P2_201314716']
        collection = db['covid']
        #collection.insert_one(data)

        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    await nc.subscribe("foo", cb=message_handler)
    await nc.flush()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()