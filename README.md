# django_celery
Cоздали приложение с помощью Django и  интегрировали Celery.

Инструкция актуальна для Linux-систем.
Используемые технологии:
    python~=3.9
    Django~=4.1
    PostgreSQL
========================================================================================================================
Скопируйте репозиторий с помощью команды:
$ git clone https://github.com/RuslanSayfullin/django_celery.git
Перейдите в основную директорию с помощью команды: 
$ cd django_celery

========================================================================================================================
Создать и активировать виртуальное окружение:
$ python -m venv venv
$ source venv/bin/activate
(venv) $

========================================================================================================================
Установить зависимости из файла requirements.txt:
$ pip install -r requirements.txt

========================================================================================================================
Создание БД

$ sudo su - postgres
Теперь запускаем командную оболочку PostgreSQL:
$ psql 

=# CREATE DATABASE django_celery;
=# CREATE USER portaluser WITH PASSWORD 'myPassword';
=# GRANT ALL PRIVILEGES ON DATABASE portal TO portaluser;
=# \q
$ exit

========================================================================================================================
Для запуска выполнить следующие команды:

Команда для создания миграций приложения для базы данных
$ python3 manage.py makemigrations
$ python3 manage.py migrate

Создание суперпользователя
$ python3 manage.py createsuperuser

Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
по умолчанию почта admin@admin.com пароль: 12345

Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.

Команда для запуска приложения
python manage.py runserver

Приложение будет доступно по адресу: http://127.0.0.1:8000/






