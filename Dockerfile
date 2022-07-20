FROM python:3.8.10-slim

RUN apt update && \
    apt install mc -y && \
    apt install vim -y

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV SECRET_KEY=django-insecure-ekaxoj%-b-t0lu^a)^&l3ej7!)9fw@ko@rnu6kvti&9zlm_2(v
ENV DEBUG=True
ENV ALLOWED_HOSTS=''

RUN mkdir /opt/src
WORKDIR /opt/src

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -f requirements.txt

COPY src .

EXPOSE 8090

CMD python manage.py runserver 0.0.0.0:8090
