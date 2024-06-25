# Django-JsonRPC

Перед запуском проекта необходимо просто в фале settings.py добавить:
```
CLIENT_CERT
CLIENT_KEY
```
Далее команда для поднятия в контейнере:
```angular2html
docker-compose up --build
```

Можно запустить в ручную:
```angular2html
poetry install
python mange.py runserver
```