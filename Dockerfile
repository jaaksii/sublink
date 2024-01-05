FROM python:3.8.13-slim
WORKDIR /app
COPY app.py .
COPY app app
COPY migrations migrations
COPY requirements.txt .
COPY uwsgi.ini .
RUN apt-get update && apt-get install -y build-essential
RUN pip3 install -r requirements.txt
RUN pip3 install setuptools wheel
RUN pip3 install uwsgi
CMD uwsgi --ini uwsgi.ini
EXPOSE 5000