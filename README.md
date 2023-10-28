
# Название проекта
    «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.

## Требования

Создайте виртуальное окружение и активируйте его:
    python -m venv venv
    venv\Scripts\activate
    pip install asgiref==3.7.2 
    pip install billiard==4.1.0 
    pip installcelery==5.3.4
    pip install Django==4.2.5 
    pip install django-celery-beat==2.5.0 
    pip install django-cors-headers==4.2.0 
    pip install django-timezone-field==6.0.1 
    pip install djangorestframework==3.14.0 
    pip install djangorestframework-simplejwt==5.3.0 
    pip install drf-yasg==1.21.7 
    pip install Pillow==10.0.1 
    pip install psycopg2==2.9.9 
    pip install psycopg2-binary==2.9.9 
    pip install pycodestyle==2.11.0 
    pip install PyJWT==2.8.0 
    pip install pyTelegramBotAPI==4.14.0 
    pip install python-crontab==3.0.0 
    pip install python-dateutil==2.8.2 
    pip install python-decouple==3.8 
    pip install python-dotenv==1.0.0 
    pip install pytz==2023.3.post1 
    pip install redis==5.0.1 
    pip install requests==2.31.0 
    pip install sqlparse==0.4.4 
    pip install tzdata==2023.3 
    pip install -r requirements.txt

Запуск
python manage.py runserver


Инструкция по запуску контейнера с проектом
docker build --no-cache -t my-python-app .
python manage.py runserver 0.0.0.0:8000   

Инструкция по запуску приложения
docker-compose build
docker-compose exec python manage.py migrate
docker-compose up

