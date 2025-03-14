FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY site /app/site

EXPOSE 5000

CMD ["python", "site/app.py"]