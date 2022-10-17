
###  *Инструкция по развёртыванию проекта*

- Клонируйте репозиторий на компьютер,
  - Сделать это можно путем введения команды в терминале.
  - ```git clone https://github.com/AlexanderPRM/Lyceum_Yandex.git``` 
- Далее вам понадобиться создать виртуальное окружение и установить зависимости для корректной работы программы.
  Откройте терминал в внешней папке "_Lyceum_Yandex_"<br>

    -  И пропишите:<br>
    Windows:
      - ```python -m venv venv```<br>
        ```venv/Scripts/activate```<br>
    Mac OS и Linux:
      - ```python3 -m venv venv```
        ```source venv/bin/activate```
    - Установка зависимостей:
      <br>```pip install -r requirements.txt```<br>
- Укажите секретные ключи.
  - В папке _lyceum_yandex_pj_ есть файл .env.exapmle, уберите расширение .example и запишите ключи в переменную SECRET_KEY и DEBUG,
    для запуска в dev-режиме в переменную DEBUG нужно указать True, иначе False
- Для того чтобы запустить "_проект_", нужно прописать команду. 
  - Также в терминале внешней папки - "Lyceum_Yandex"
  - ```python lyceum_yandex_pj/manage.py runserver```
