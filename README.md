<p align="center">

<img height="520em" src=https://github.com/PARTYNEXTDOORS/shop_bot_aiogram/assets/103187040/f012ae1c-b1e5-444f-bf2e-fde10e52e0a2 />
<img height="520em" src=https://github.com/PARTYNEXTDOORS/shop_bot_aiogram/assets/103187040/f491a908-8ac2-4d7e-a556-82ca04584627 />

</p>

____

<h1 align="left" id="macropower-title">Телеграм бот магазин </h1>

____

## Описание проекта:
Магазин бот с возможностью добавления в группы, фильтром мата. Новые товары добавляются вручную через админку бота. Запуск бота реализован через `bat` файл. Чтобы подключить оплату, смотрите [подключение qiwi](https://github.com/PARTYNEXTDOORS/qiwi_pay_bot) или через [платежный шлюз телеграм](https://github.com/PARTYNEXTDOORS/pay_bot_aiogram).

____

## Запуск проекта на локально сервере
Для начала стоит [создать бота](https://chatlabs.ru/botfather-instrukcziya-komandy-nastrojki/).
+ склонировать репозиторий
```
git clone git@github.com:PARTYNEXTDOORS/shop_bot_aiogram.git
```
+ установить вирутиальное окружение
```
python -m venv venv`(для Windows)
python3 -m venv env`(для Mac/Linux)
```
+ активировать виртуальное окружение
```
source venv/Script/activate`(для Windows)
source venv/bin/activate`(для Mac/Linux)
```
+ установаить бибилиотеку aiogram
```
pip install aiogram
```
+ далее в дирректории выше `cd ..` создаем файл txt с расширением bat `bot_run.bat` и пишем в нем следующее
```
@echo off

call %~dp0shop_bot_aiogram/venv/Scripts/activate  # активируем виртуальное окружение

cd %~dp0shop_bot_aiogram  # путь к файлу

set TOKEN=здесть должен быть ваш токен

python bot.py  # запускаем бота

pause
```
+ запускаем bat файл
+ далее подключаем нашего бота к группе в телеграм и даем ему права администратора. Чтобы заполнить магазин товарами в группе вводим команду
```
/moderator
```
+ нас перенаправляет в бота для заполнения магазина
<p align="center">
  <img height="520em" src=https://github.com/PARTYNEXTDOORS/shop_bot_aiogram/assets/103187040/be2cd72e-2ab7-4276-9c7a-de11423daa2b />
</p>
+ следуя инструкциям заполняем карточку
<p align="center">
  <img height="520em" src=https://github.com/PARTYNEXTDOORS/shop_bot_aiogram/assets/103187040/4e58e3f9-cabf-45ad-8d35-cf25d60d5439 />
</p>
+ и получаем результат
<p align="center">
  <img height="520em" src=https://github.com/PARTYNEXTDOORS/shop_bot_aiogram/assets/103187040/e88f6c0a-a2db-471f-9bb3-bcbb10d7783c />
</p>
