# Jump into Django

Учебный проект ACME на Django 5.2. Главная страница и каталог показывают демонстрационные товары. Приложение `cinema` содержит две связанные модели; пользовательского интерфейса для них пока нет.

## Локальный запуск

Из папки `acme_project` с Python 3.13:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r ..\requirements.txt
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py runserver
```

Откройте `http://127.0.0.1:8000/` или `http://127.0.0.1:8000/catalog/`. Каталог использует данные в `catalog/views.py`; они не хранятся в базе. Папка `static_dev/` подключена как источник статических файлов.

Проверки: `.venv\Scripts\python.exe manage.py check` и `.venv\Scripts\python.exe manage.py test`. Команда `migrate` создаёт локальную базу SQLite при отсутствии файла; существующая база в этой работе не изменялась.

Для локальной разработки переменные окружения необязательны: по умолчанию включён `DEBUG` и при каждом запуске создаётся временный ключ. Для постоянных сессий задайте `DJANGO_SECRET_KEY`. При `DJANGO_DEBUG=false` ключ обязателен; `DJANGO_ALLOWED_HOSTS` принимает список хостов через запятую. `.env.example` служит примером и не загружается Django автоматически. Эти настройки предназначены для локального учебного запуска.
