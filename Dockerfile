FROM python:3-alpine

RUN apk update

COPY . /container
WORKDIR /container

RUN pip install -r requirements.txt

CMD pytest -v -s -m regression