FROM python:3.8.13-slim
WORKDIR /app
COPY app.py .
COPY app app
COPY migrations migrations
COPY requirements.txt .
COPY uwsgi.ini .
COPY docker-compose.yml .
RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Shanghai
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
ENV PORT=5000
CMD uwsgi --ini uwsgi.ini --http-socket=0.0.0.0:${PORT}
EXPOSE ${PORT}

