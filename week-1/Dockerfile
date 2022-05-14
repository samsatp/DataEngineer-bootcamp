FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy pgcli

WORKDIR /app
COPY . .

ENTRYPOINT ["python","ingestion.py"]