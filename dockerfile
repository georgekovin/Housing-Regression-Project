FROM python:3.11

WORKDIR /src/app

COPY ./app ./
COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

