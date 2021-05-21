# Проект Interview 
API для системы опросов пользователей

<p align="center">
<img src="https://user-images.githubusercontent.com/68146917/119162673-54131f00-ba63-11eb-9ecb-c9086568f58e.png">
</p>

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)


## Техническое описание
___

Администрирование системы:
+ Авторизация в системе.

+ Опросы:
    + Добавление.
    + Изменение.
    + Удаление опросов
+ Вопросы
    + Добавление.
    + Изменение.
    + Удаление Вопросов

Функционал для пользователей системы:

+ Получение списка активных опросов
+ Прохождение опроса
+ Получение пройденных пользователем опросов с детализацией по ответам

## Системные трубования
______

- [Python 3](https://www.python.org/)
- [Django 2.2.10](https://www.djangoproject.com/)
- [REST API Framework](https://www.django-rest-framework.org/)
- [NGINX](https://www.nginx.com/)
- [Gunicorn](https://gunicorn.org/)
- [Docker](https://www.docker.com/)
- [PostgrSQL](https://www.postgresql.org/)


## Работа с API
___

Просмотреть список доступных опросов можно по URL /api/v1/polls/. Используйте GET запрос

Список будет доступен в следующем виде:

![](https://user-images.githubusercontent.com/68146917/119164356-039cc100-ba65-11eb-9c16-db52e45c651b.png)


Вопросы по опросу доступны по URL /api/v1/polls/<Номер опроса>/questions/

Пример:
http://127.0.0.1/api/v1/polls/1/questions/

Список вопросов будет доступен в следующем виде:

![](https://user-images.githubusercontent.com/68146917/119165518-3abfa200-ba66-11eb-95da-d6aed1e4be10.png)

Варианты ответов указываются ниже.

Что-бы принять участие в опросе, отправьте пустой POST запрос на URL /api/v1/polls/номер-опроса/questions/


Ответ на вопрос. POST запрос, поле answer, URL - номер вопроса/answers/

Пример:

![Screenshot 2021-05-21 at 19 04 53](https://user-images.githubusercontent.com/68146917/119166549-6ee79280-ba67-11eb-8d47-abbca26d85c5.png)

Увидеть свои результаты  - GET запрос URL api/v1/me/

Пример:

![](https://user-images.githubusercontent.com/68146917/119168126-406ab700-ba69-11eb-86b5-d36c9b326fb1.png)


## Администрирование
___

```
/api/v1/admin/poll/ GET/POST/PUT/PATCH - добавление/изменение опросов
```

```
/api/v1/admin/poll/<pull_id>/questions/ GET/POST/PUT/PATCH - добавление/изменение вопросов
```

```
/api/v1/admin/poll/<pull_id>/questions/<q_id>/answers/ GET/POST/PUT/PATCH - добавление/изменение ответов
```

В проекте настроена админка.


## Запуск проекта
___


В терминале выполните команду

```
https://github.com/Gilions/Interview.git
```

В корне проекта создайте .env, со следующим содержанием:

```
SECRET_KEY='qc74day!hei!a5u#(p(bijbc87^lawnonrfk!-4(0_ue4k$wf2'

#Postgres setting
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=Your password
DB_HOST=db
DB_PORT=5432
```

Запустить команду

```
docker compose up
```

Создать superuser можно в docker контейнере. Используйте компанду
```
docker exec -it <Номер контейнера> bash
```
Самом контейнере используйте команду:
```
python manage.py createsuperuser
```


Сайт будет доступен по URL http://127.0.0.1/

