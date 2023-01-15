FROM python:3.10.9-bullseye

WORKDIR /home/eugene
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install mysql-connector-python
RUN pip install jupyter
COPY . .
