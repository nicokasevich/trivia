FROM python:3.8.10

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--nostatic"]