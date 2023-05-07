FROM python:3
MAINTAINER Eric Dantas <ericrommel@gmail.com>

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=run
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_CONFIG=development
ENV SRC_ENV=/var/www

WORKDIR ${SRC_DIR}/

COPY ./requirements.txt ${SRC_DIR}/requirements.txt

RUN ["pip", "install", "-r", "requirements.txt"]

COPY . ${SRC_DIR}/

RUN ["flask", "db", "init"]
RUN ["flask", "db", "migrate"]
RUN ["flask", "db", "upgrade"]
CMD ["flask", "run"]
