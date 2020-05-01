# start from an official image
FROM python:3.7-alpine

RUN mkdir -p /home/covid
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./covid /home/covid
WORKDIR /home/covid

# expose the port 5000
EXPOSE 5000