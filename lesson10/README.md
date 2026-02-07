# Lesson 10: Тестирование SauceDemo

## Описание
Проект содержит E2E тест покупки товара в магазине SauceDemo.
Используется паттерн PageObject, библиотека Allure для отчетов и аннотации типов.

## Структура
- `pages/` - описание страниц (Page Objects)
- `test_saucedemo_total.py` - основной тест

## Запуск тестов
1. Установите зависимости:
   `pip install pytest selenium allure-pytest webdriver-manager`

2. Запустите тесты из корня проекта:
   `pytest lesson10/ --alluredir=result`

3. Посмотрите отчет:
   `allure serve result`
