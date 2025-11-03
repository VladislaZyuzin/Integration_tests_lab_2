# Лабораторная работа №2 (Simple Flask API)
> Выполнил Зюзин Влалислав №3320

Этот проект представляет собой простой REST API на Python и Flask для получения данных о книгах из базы данных SQLite3. Ссылка на репу с которой был сделан форк - в проекте

## Что было сделано в лабораторной работе

В этой лабораторной работе были написаны интеграционные тесты, проверяющие взаимодействие API с базой данных.

Выполненные шаги:

1. Сделан форк и клонирование исходного репозитория.
2. Настроено виртуальное окружение (venv) и установлены зависимости (Flask, pytest и др.).
3. Созданы интеграционные тесты с использованием pytest для проверки работы API:
* GET `/api/v2/resources/books/all` — получение всех книг.
* GET `/api/v2/resources/books?author=<имя>` — фильтрация книг по автору.
* GET `/api/v2/resources/books?published=<год>` — фильтрация книг по году издания.
4. Тестировались сценарии пустого результата и обращения к несуществующему маршруту.
5. Запуск тестов в виртуальном окружении:
```bash
python -m pytest -v
```
Все 5 интеграционных тестов прошли успешно, что подтверждает корректную работу API.

Пример вывода тестов:

<img width="592" height="500" alt="image" src="https://github.com/user-attachments/assets/42632473-3f6b-4e5d-9cc1-5960f0bf86be" />

## Как использовать

Клонировать проект:
```bash
git clone https://github.com/VladislaZyuzin/simple-flask-api-forlab2.git
cd simple-flask-api-forlab2
```
Создать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:
```bash
pip install -r requirements.txt
pip install pytest
```

Запустить API:
```
python app.py
```
### Примеры запросов к API

Получить все книги:
```
http://127.0.0.1:5000/api/v2/resources/books/all
```

<img width="742" height="690" alt="image" src="https://github.com/user-attachments/assets/6f302f80-e719-422d-938f-6925e836d000" />


### Получить книги автора Connie Willis:
```
http://127.0.0.1:5000/api/v2/resources/books?author=Connie+Willis
```

<img width="742" height="180" alt="image" src="https://github.com/user-attachments/assets/84166dbd-4b09-408f-bbd1-b11fcda840cb" />


Получить книги, изданные в 2010 году:
```
http://127.0.0.1:5000/api/v2/resources/books?published=2010
```

<img width="742" height="180" alt="image" src="https://github.com/user-attachments/assets/707a9368-c869-4e5e-89bf-8b26e716c3a7" />


## Интеграционные тесты

Интеграционные тесты проверяют полное взаимодействие между Flask API и базой данных SQLite.
Все тесты находятся в файле tests/test_integration_api_db.py и запускаются командой:

```bash
python -m pytest -v
```

Все тесты прошли успешно, что подтверждает корректную работу API.
