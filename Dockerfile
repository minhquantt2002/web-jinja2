FROM python:lastest
WORKDIR /app

COPY requirements.txt /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD uvicorn 'app.main:app' --host=0.0.0.0 --port=8000
