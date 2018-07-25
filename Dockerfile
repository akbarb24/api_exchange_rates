FROM python:2.7.15

EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD python run.py