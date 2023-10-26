FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip
    
WORKDIR /flask-app
VOLUME /flask-app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
ENV FLASK_APP=app.py

CMD [ "python", "app.py"]
