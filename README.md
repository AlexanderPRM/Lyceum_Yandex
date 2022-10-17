
###  *Инструкция по развёртыванию проекта*

- Клонируйте репозиторий на компьютер,
  - Сделать это можно путем введения команды в терминале.
  - ```git clone https://github.com/AlexanderPRM/Lyceum_Yandex.git``` 
- Далее вам понадобиться установить зависимости для корректной работы программы и указать секретные ключи.
  - Откройте терминал в основной папке "_Lyceum_Yandex_"<br>
    -  И пропишите - ```pip install -r requirements.txt```<br>
  - В папке _lyceum_yandex_pj_ есть файл .env.exapmle, уберите расширение .example и запишите ключи в переменную SECRET_KEY и DEBUG,
    для запуска в dev-режиме в переменную DEBUG нужно указать True, иначе False
- Для того чтобы запустить "_проект_", нужно прописать команду.
  - Также в терминале основной папки - "Lyceum_Yandex"
  - ```python lyceum_yandex_pj/manage.py runserver```
