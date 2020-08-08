FROM python:3.8-slim

WORKDIR /cloud_proj

COPY . /cloud_proj

RUN pip install -r requirements.txt

CMD flask run --host:0.0.0.0 --port=8080

