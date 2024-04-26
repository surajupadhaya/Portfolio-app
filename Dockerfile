FROM python:3.11-alpine
MAINTAINER suraj upadhaya
RUN mkdir /portfolio-app

WORKDIR /portfolio-app

COPY . /portfolio-app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python", "./app.py" ]
