FROM python

RUN python -m pip install --upgrade pip

RUN pip install asyncio-nats-client

RUN python -m pip install pymongo

COPY ./app /app

WORKDIR /app

CMD [ "python", "main.py" ]