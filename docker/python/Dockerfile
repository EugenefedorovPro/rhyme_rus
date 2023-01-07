FROM python:3.10.9-bullseye

RUN apt-get update && apt-get install -y git
WORKDIR /home/eugene
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install jupyter
COPY . .