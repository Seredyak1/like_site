FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN apt-get update && apt-get install -y netcat && \
    apt-get install -y libpq-dev python3-dev

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
RUN ["chmod", "+x", "entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
