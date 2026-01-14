FROM python:3.10
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install -y awscli && pip install -r requirements.txt
CMD ["python3", "app.py"]