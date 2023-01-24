FROM python:3.10.9-buster
WORKDIR /home/eugene
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
COPY . .
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]