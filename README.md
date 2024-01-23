# Задача
Актуальный курс доллара к рублю

#### Список технологий: Python, Django DRF,Celery,Redis


## Подготовка и запуск проекта
#### Шаг 1. Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
```bash
docker -v
```
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 2. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/currency.git
```


#### Шаг 3. Создайте в клонированной директории(currency_rate/.env) файл .env
Пример:
```bash

KEY_API=58cf8eefee2419244c06c43213de050118518ce1 # для тестирования можете использовать 

```
#### Установка и создание виртуального окружения
- Откройте терминал или командную строку
- Перейдите в каталог, где вы хотите создать виртуальное окружение
- Введите следующую команду:
```python
    python3 -m venv venv
```
- Активация виртуального окружения
```python
Windows:

myenv\Scripts\activate

macOS и Linux:

source myenv/bin/activate


```


#### Шаг 4.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```
#### Шаг 5.Создаем  суперюзера для входа в Django Admin
```python
    python manage.py createsuperuser
```
#### Шаг 6. Выполняем комманду
```python
    pip install -r requirements.txt
```
#### Шаг 7. Запуск Redis через Docker
```
 Для Windows в CMD:
    1.pull redis  
    2.docker run -d -p 6379:6379 --name redis
 
```
#### Шаг 8. После успешной установки запускаем сервер 
```python
    python manage.py runserver
    celery -A currency_project beat --loglevel=info
    celery -A currency_project worker --loglevel=info

```

## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).
### Получение данных
```json
GET  http://127.0.0.1:8000/get-current-usd/
```