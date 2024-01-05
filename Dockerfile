FROM python:3.8.13-alpine

WORKDIR /app

COPY app.py .
COPY app app
COPY migrations migrations
COPY requirements.txt .
COPY uwsgi.ini .
RUN apk update \
    && apk add --no-cache build-base \
    && pip install --upgrade pip \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && apk del build-base \
    && rm -rf /var/cache/apk/*

CMD uwsgi --ini uwsgi.ini

EXPOSE 5000
