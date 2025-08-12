# Обучаемые VK и TG боты для тех.поддержки

Этот проект содержит двух ботов — для Telegram и VK.
Боты принимают сообщения от пользователей, обрабатывают их через Google DialogFlow и возвращают осмысленные ответы.

## Примеры:
VK: 

![Демо вк бота](https://github.com/user-attachments/assets/b1ee5203-abd8-4285-ace7-80dff030e4b2)

TG:

![Демо тг бота](https://github.com/user-attachments/assets/34031c70-7127-4aad-8e5f-b3709e7a6a7e)

## Требования

Для запуска скрипта необходимы:

- Python 3.8+
- Установленные зависимости из `requirements.txt`

## Установка

1. Склонируйте репозиторий проекта:
    ```bash
    git clone https://github.com/GoNt1eRRR/talk_bot.git
    ```

2. Создайте виртуальное окружение:
    ```bash
    python -m venv .venv
    ```

3. Активируйте виртуальное окружение:
    - На Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - На Linux и MacOS:
        ```bash
        source .venv/bin/activate
        ```

4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Конфигурация
1. Получите токен для тг бота через [BotFather](https://telegram.me/BotFather)
   
2. Получите токен для вк бота в меню “Работа с API” в настройках вашего сообщества

3. PROJECT_ID который вы получили, когда создавали проект на Google Project (Пример encoded-zoo-46)

4. GOOGLE_APPLICATION_CREDENTIALS - переменная окружения, где лежит путь до файла с ключами от Google, credentials.json. Подробнее читать [здесь](https://cloud.google.com/docs/authentication/api-keys)
   
**Бот не будет работать без токенов!**

Создайте файл `.env` в корне проекта и добавьте туда ваши данные. 

Пример файла `.env`:

```
TG_TOKEN= Ваш тг токен
GOOGLE_APPLICATION_CREDENTIALS= Путь файла с ключами от гугл
PROJECT_ID= название проекта на Google Project
VK_TOKEN= Ваш вк токен
```

## Запуск 
Запуск скриптов осуществляется через консоль:
```
python tg_bot.py
python vk_bot.py
```

## Обучение ботов
Обучение осуществляется через сервис DialogFlow. Так же необходимо создать агента, которого нужно подключить к проекту DialogFlow для автоматизации обучения используйте скрипт create_intents.py. Функция create_intent необходима для обучения бота. Более подробное описание работы функций можно прочитать [здесь](https://cloud.google.com/dialogflow/es/docs/how/manage-intents#create_intent)

## Цель проекта
Проект создан в образовательных целях
