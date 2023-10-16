FROM python:3.11.5

WORKDIR /flask-app

COPY ./requirements.txt .

RUN apt install -y build-essential libssl-dev libffi-dev libxml2 libxslt1-dev zlib1g-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
ENV FLASK_APP=app.py

CMD [ "python", "app.py"]
