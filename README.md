# CyberPhysLab2
Лабораторные работы по кибер-физическим системам, вариант 2

## Запуск
1. Сборка и запуск контейнера:
   `docker-compose up --build`
2. Запуск тестового клиента:
   `python client.py`

## Результаты тестирования

```text
=====================================================================================
                 SMS SPAM DETECTION SYSTEM PERFORMANCE REPORT                  
=====================================================================================
№   | SMS Message Text                                             | Verdict
-------------------------------------------------------------------------------------
1   | URGENT! You have won a 1-week HALO ticket. Call 090617014..  | SPAM (1) [0.39s]
2   | Hi! Are you coming to the party tonight? Let me know.        | OK   (0) [0.28s]
3   | FREE entry into our £250 weekly competition. Text WIN to ..  | OK   (0) [0.31s]
4   | I'll be home in 10 minutes. Can you start the kettle?        | OK   (0) [0.28s]
5   | Your account #1234 has a security alert. Log in at bit.ly..  | SPAM (1) [0.32s]
6   | Could you please send me the report by EOD? Thanks.          | OK   (0) [0.30s]
7   | CONGRATULATIONS! You've been selected for a $1000 Walmart..  | SPAM (1) [0.32s]
8   | Don't forget our dental appointment at 4 PM tomorrow.        | OK   (0) [0.27s]
9   | Get a loan today with 0% interest! No credit check needed..  | OK   (0) [0.30s]
10  | Hey, can you call me back when you have a second?            | OK   (0) [0.29s]
-------------------------------------------------------------------------------------
```
Как видно,некоторые очевидные СПАМ сообщения не распознаются, а НЕ СПАМ ложно объявлены спамом. Это из-за слабой модели. И тем не менее, это работает как proof-of-concept. 

## Вывод
В ходе лабораторной работы был успешно реализован Proof-of-Concept системы классификации СМС. Система контейнеризирована и общается по HTTP. Низкое качество распознавания спама обусловлено малым размером выбранной модели (Qwen2.5:0.5B — 500 млн параметров). Для вывода системы в Production (production-ready) достаточно заменить модель на более крупную (например, 8B или 70B параметров) без изменения архитектуры микросервиса.
