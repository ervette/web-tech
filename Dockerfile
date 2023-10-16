FROM python:latest

WORKDIR /flask-app

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
ENV FLASK_APP=app.py

CMD [ "python", "app.py"]
