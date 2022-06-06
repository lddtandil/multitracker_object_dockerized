#First Stage
FROM python:3.8 AS builder
MAINTAINER Leonardo Daniel Dominguez "leonardodanieldominguez@gmail.com"
ENV TZ "America/Argentina/Buenos_Aires"
COPY requirements.txt .

RUN pip install --upgrade pip --user -r  requirements.txt

#Seconds Stage
FROM python:3.8-slim
WORKDIR /code
#Libglib2.0-0 is not included in slim images
RUN apt update && apt-get install -y libglib2.0-0 
#Copy the builder installation dependencies
COPY --from=builder /root/.local /root/.local
COPY ./src .

ENV PATH=/root/.local:$PATH
ARG VIDEO_NAME
ENV VIDEO_NAME=$VIDEO_NAME
ARG JSON_NAME
ENV JSON_NAME=$JSON_NAME
ARG TRACKER_NAME
ENV TRACKER_NAME=$TRACKER_NAME

CMD ["sh", "-c", "python ./main.py $VIDEO_NAME $JSON_NAME $TRACKER_NAME"]

