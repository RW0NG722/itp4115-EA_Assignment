FROM python:3.12.6-slim

COPY app.py /src/app.py
COPY models.py /src/models.py
COPY requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
