FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80


RUN mkdir /app
COPY ./app /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
