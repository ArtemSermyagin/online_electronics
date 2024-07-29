Проект "online_electronics" представляет собой веб-приложение для управления цепочкой розничной торговли электроникой, с API-интерфейсом и админ-панелью

Установка
Для того чтобы развернуть проект локально, выполните следующие шаги:

Создайте виртуальное окружение и активируйте его: python -m venv venv / source venv/bin/activate # On Windows use venv\Scripts\activate
Установите зависимости: pip install -r requirements.txt
Выполните миграции базы данных: python manage.py migrate
Создайте суперпользователя для доступа к админ-панели: python manage.py createsuperuser
Запустите сервер разработки: python manage.py runserver
В директории проекта создать файл .env на основе .env.example: Записать в файл следующие настройки:
SECRET_KEY=секретный код джанго
POSTGRES_DB=название базы данных
POSTGRES_USER=имя пользователя в базе данных
POSTGRES_PASSWORD=пароль пользователя в базе данных
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

Теперь приложение должно быть доступно по адресу http://127.0.0.1:8000/

Использование
Админ-панель
Админ-панель доступна по адресу http://127.0.0.1:8000/admin/ Используйте учетные данные суперпользователя для входа.

API
API эндпоинты доступны по адресу http://127.0.0.1:8000/

Функции
Управление поставщиками
Управление товарами
Управление заказами
Админ-панель для управления данными
API для взаимодействия с внешними приложениями
Просмотр документации