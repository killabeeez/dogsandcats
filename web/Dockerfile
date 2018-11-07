FROM alpine

RUN mkdir -p /data/web
WORKDIR /data/web

COPY requirements.txt /data/web/

RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-dev build-base gettext jpeg-dev zlib-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN apk del -r python3-dev postgresql

COPY . /data/web/

