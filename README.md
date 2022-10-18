![flake8 status](https://github.com/AlexanderPRM/Lyceum_Yandex/actions/workflows/python-package.yml/badge.svg?event=push)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![rating](https://img.shields.io/badge/rating-★☆☆☆☆-brightgreen)&nbsp;&nbsp;
[![telegram-dev](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/permyakov10)
###  *Инструкция по развёртыванию проекта*

- Клонируйте репозиторий на компьютер,
  - Сделать это можно путем введения команды в терминале.
  - ```git clone https://github.com/AlexanderPRM/Lyceum_Yandex.git``` 
- Далее вам понадобиться создать виртуальное окружение и установить зависимости для корректной работы программы.
  Откройте терминал в внешней папке "_Lyceum_Yandex_"<br>
    -  И пропишите:<br>
    Windows:
      <br>```python -m venv venv```<br>
        ```venv/Scripts/activate```<br>
    Mac OS и Linux:
      <br>```python3 -m venv venv```<br>
        ```source venv/bin/activate```
    - Установка зависимостей:
      <br>```pip install -r requirements.txt```<br>
- Укажите секретные ключи.
  - В папке _lyceum_yandex_pj_ есть файл .env.exapmle, уберите расширение .example и запишите ключи в переменную SECRET_KEY и DEBUG,
    для запуска в dev-режиме в переменную DEBUG нужно указать True, иначе False
- Для того чтобы запустить "_проект_", нужно прописать команду. 
  - Также в терминале внешней папки - "Lyceum_Yandex"
  <br>Windows:<br>
  ```python lyceum_yandex_pj/manage.py runserver```
  <br>Mac OS и Linux:<br>
  ```python3 lyceum_yandex_pj/manage.py runserver```
  
