FROM alexberkovich/alpine-anaconda3:latest

WORKDIR /flask-app

COPY ./requirements.txt .

#RUN pip install --upgrade pip

#RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev libxml2 libxslt1-dev zlib1g-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
ENV FLASK_APP=app.py

CMD [ "python", "app.py"]
