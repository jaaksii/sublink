FROM python:3.8.13-slim
WORKDIR /app
MAINTAINER 坤坤 tg:@toute_1
COPY app.py .
COPY app app
COPY migrations migrations
COPY requirements.txt .
COPY uwsgi.ini .
RUN apt-get update && apt-get install -y build-essential
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install --upgrade setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install uwsgi
EXPOSE 5000

