from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from create_bot import bot
from keyboards import kb_client
from data_base import sqlite_db


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита',
                               reply_markup=kb_client)
        await message.delete()
    except IndexError:
        await message.reply('Общение с ботом через ЛС, напишите ему:'
                            'https://t.me/Pizzas_sdsdfBot')


async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Пн-Пт с 9:00 до 19:00, Пт-Сб с 10:00 до 23:00')


async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'проспект Мира 18',
                           reply_markup=ReplyKeyboardRemove())


async def pizzas_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])
    dp.register_message_handler(place_command, commands=['Расположение'])
    dp.register_message_handler(pizzas_menu_command, commands=['Меню'])
