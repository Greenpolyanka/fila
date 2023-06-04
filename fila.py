import telebot
from telebot import types
import logging
import asyncpg
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import psycopg2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from psycopg2 import extensions

host = '10.40.240.85'
port = '5432'
user = 'student'
password = 'student-rtf-123'
database = 'RI_211055_Kameneva_PD'

bot = Bot(token = '6055998098:AAEIhwECL5vI_PZBLvszTJh6tSMEUX2O3bA')

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot, storage=MemoryStorage())

role_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
role_keyboard.add(KeyboardButton('Расписание мероприятий'))


role_keyboard.add(KeyboardButton('Залы'))
role_keyboard0.add(KeyboardButton('Узнать информацию о зале'))
role_keyboard.add(KeyboardButton('Выбрать тип мероприятия'))

role_keyboard1.add(KeyboardButton('Отчетный концерт'))
role_keyboard1.add(KeyboardButton('Гала-концерт'))
role_keyboard1.add(KeyboardButton('Конкурс'))
role_keyboard2.add(KeyboardButton('Информация о призерах'))
role_keyboard1.add(KeyboardButton('Симфонический концерт'))
role_keyboard1.add(KeyboardButton('Спектакль'))
role_keyboard1.add(KeyboardButton('Хоровой концерт'))
role_keyboard1.add(KeyboardButton('Камерный концерт'))

role_keyboard.add(KeyboardButton('Внести себя в списки артистов'))



@bot.messege_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет, я бот филармонии. Что бы вы хотели сделать:", reply_markup=role_keyboard)

async def send_message_with_limit(chat_id, message_text):
    if len(message_text) <= 4096:
        await bot.send_message(chat_id, message_text)
    else:
        parts = [message_text[i:i+4096] for i in range(0, len(message_text), 4096)]
        for part in parts:
            await bot.send_message(chat_id, part)
    

@dp.message_handler(lambda message: message.text == 'Расписание мероприятиий')
async def handler_chose_mero(message: types.Message, state: FSMContext):
    conn = psycopg2.connect(database=postgres, user=student, password=student-rtf-123, host=10.40.240.85, port=5432)
    cursor = conn.cursor()
    try:
        cursor.execute('SET search_path to fila; SELECT * FROM мероприятия(название_мероприятия,дата_мероприятия,id_зала)
        rows = cursor.fetchall()

        response = 'Мероприятия и их расписание:\n\n'
        for row in rows:
            mero_str = f"Название: {row[0]}\nДата: {row[1]}\n\n"
            response += mero_str

        await send_message_with_limit(message.chat.id, response)

    except psycopg2.Error as e:
        print("Ошибка при выполнении запроса:", e)
        await message.answer("Произошла ошибка при получении информации о мероприятиях.")

    cursor.close()
    conn.close()


if __name__ == '__main__':
    logging.info("Бот запущен!")
    executor.start_polling(dp)