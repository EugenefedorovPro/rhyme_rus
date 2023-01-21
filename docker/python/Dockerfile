FROM python:3.10.9-bullseye
WORKDIR /home/eugene
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install jupyter
COPY . .
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]