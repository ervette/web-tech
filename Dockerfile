FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y pip python3-dev build-essential libssl-dev libffi-dev libxml2 libxslt1-dev zlib1g-dev

WORKDIR /flask-app
VOLUME /flask-app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
ENV FLASK_APP=app.py

CMD [ "python", "app.py"]
