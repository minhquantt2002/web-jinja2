FROM python:lastest
WORKDIR /app

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn 'app.main:app' --host=0.0.0.0 --port=8000
