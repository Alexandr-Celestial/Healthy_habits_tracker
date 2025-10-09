# Healthy_habits_tracker

Проект Django REST API для управления привычками с интеграцией Telegram-бота и системой напоминаний через Celery.

## Описание

Это серверная часть приложения для трекинга привычек,
где пользователь может создавать полезные и приятные привычки с расписанием,
получать напоминания в Telegram и управлять своими данными через API.

## Основные возможности

+ Пользовательская регистрация и аутентификация по email
+ CRUD API для привычек с валидацией и правами доступа
+ Публичный список привычек
+ Интеграция с Telegram-ботом для получения напоминаний
+ Асинхронная отправка напоминаний через Celery + Redis
+ Автоматическая документация API Swagger (drf_yasg)
+ Полная настройка CORS для фронтенда
+ Покрытие тестами не менее 80%

## Миграции и запуск сервера

```python manage.py migrate```
```python manage.py runserver```

## Запуск Celery и Celery Beat

```celery -A config worker -l info```
```celery -A config beat -l info```

## Документация API

Доступна по адресам:

+ Swagger UI: http://localhost:8000/swagger/
+ Redoc: http://localhost:8000/redoc/

## Структура проекта

+ users/ — модели, сериализаторы, вью для пользователей
+ habits/ — модели, API и логика привычек
+ bot/ — интеграция с Telegram и менеджмент-команды
+ config/ — настройки проекта, celery и маршруты
+ requirements.txt — список зависимостей

## Установка и Запуск:

Данный проект использует Poetry для управления зависимостями.

1. Клонируйте репозиторий:

   ```
   git clone git@github.com:Alexandr-Celestial/Healthy_habits_tracker.git
   cd drf_atomic_habits
   ```

2. Создайте и активируйте виртуальное окружение:

   ```
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   # venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости с помощью Poetry:
   ```poetry install```
4. Настройте переменные окружения. Рекомендуется использовать файл .env и установить переменную DJANGO_SETTINGS_MODULE в
   соответствии с вашим файловым путем.
5. Примените миграции базы данных:
   ```poetry run python manage.py migrate```
6. Запустите сервер разработки Django:
   ```poetry run python manage.py runserver```
7. Для работы напоминаний и отложенных задач, запустите Celery worker:
```poetry run celery -A drf_atomic_habits.celery worker -l info```
8. Для запуска всех тестов:
```poetry run python manage.py test```

## Запуск проекта с использованием Docker Compose
Этот файл docker-compose.yml определяет конфигурацию для запуска всех необходимых сервисов вашего проекта:
веб-приложения Django, базы данных PostgreSQL, Redis и Celery (worker и beat).

## Предварительные требования
- Docker установлен и работает.
- Docker Compose установлен (обычно входит в состав Docker Desktop).
- Файл .env с необходимыми переменными окружения (например, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD).

## Процесс запуска

1. Сборка и запуск всех сервисов
   Перейдите в корневую директорию проекта. Затем выполните следующую команду:

```docker-compose up --build``` или ```docker-compose -f docker-compose.yml up```