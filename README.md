##### _разработка Sayfullin R.R.

Инструкция актуальна для Linux-систем.
========================================================================================================================
Используемые технологии:
    python = "^3.11.11"
    fastapi = "^0.115.12"
    PostgreSQL

Скопируйте репозиторий с помощью команды:
$ git clone https://github.com/RuslanSayfullin/FastAPI-Cookbook.git
Перейдите в основную директорию с помощью команды: 
$ cd FastAPI-Cookbook

========================================================================================================================
Создать и активировать виртуальное окружение: 
    $ python3 -m venv venv 
    $ source venv/bin/activate 
Установить зависимости из файла requirements.txt:
    (venv) $ pip install -r requirements.txt

Cоздания файла зависимостейс помощью команды:
    $ pip freeze > requirements.txt

Open the inreactive documentation: http://localhost:8000/docs

# Источник
========================================================================================================================
https://github.com/PacktPublishing/FastAPI-Cookbook


Chapter 1, First Steps with FastAPI
Chapter 2, Working with Data
Chapter 3, Building RESTful APIs with FastAPI
Chapter 4, Authentication and Authorization
Chapter 5, Testing and Debugging FastAPI Applications
Chapter 6, Integrating FastAPI with SQL Databases
Chapter 7, Integrating FastAPI with NoSQL Databases
Chapter 8, Advanced Features and Best Practices
Chapter 9, Working with WebSocket
Chapter 10, Integrating FastAPI with other Python Libraries
Chapter 11, Middleware and Webhooks
Chapter 12, Deploying and Managing FastAPI Applications