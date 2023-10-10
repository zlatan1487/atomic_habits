FROM python:3

WORKDIR /app

COPY ./requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt || echo "Failed to install requirements"

COPY . .


CMD ["python", "manage.py", "runserver", "--bind", "0.0.0.0:8000"]
