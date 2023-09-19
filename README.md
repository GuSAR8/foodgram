Foodgram

Описание

Проект "Продуктовый помошник" (Foodgram):
  
Для запуска требуется установить Docker и Docker Compose

Клонируем репозиторий:
```
git@github.com:GuSAR8/foodgram-project-react.git
```

Проект использует базу данных PostgreSQL.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env"

Пример файла ".env", можно посмотреть в ".env.example":
```python
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
POSTGRES_DB=foodgram
DB_NAME=foodgram
DB_PORT=5432
DB_HOST=db
ALLOWED_HOSTS='Здесь указать имя или IP хоста' (Для локального запуска - 127.0.0.1)
SECRET_KEY='Здесь указать секретный ключ'
DEBUG=False
```

Команды для запуска

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/GuSAR8/foodgram-project-react.git
SSH: git clone git@github.com:GuSAR8/foodgram-project-react.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Собрать образы для фронта и бэка.  
Из папки "./backend/foodgram/" выполнить команду:
```bash
docker build -t gusar8/foodgram_backend .
```

Из папки "./frontend/" выполнить команду:
```bash
docker build -t gusar8/foodgram_frontend .
```

Cоздать и запустить контейнеры.  
Из папки "./infra/" выполнить команду:
```bash
docker-compose up -d
```

Выполнить миграции:
```bash
docker-compose exec backend python manage.py migrate
```

Создать суперюзера:
```bash
docker-compose exec backend python manage.py createsuperuser
```

Собрать статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```
  
Заполнить базу данных ингредиентами:
```bash
docker-compose exec backend python manage.py load_ingredients
```

Заполнить базу данных тэгами:
```bash
docker-compose exec backend python manage.py load_tags
```


Техническая информация

Стек технологий: Python 3, Django, Django Rest Framework, Docker, PostgreSQL, nginx, gunicorn, Djoser.


Информация для ревьюера:
URL: https://foodgram2023.servebeer.com/
Login: Max
Password: MKolodnikoff
