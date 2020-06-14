FROM python:3

COPY . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "app/src/app.py"]

