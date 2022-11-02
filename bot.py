import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)


TOKEN = '5746104623:AAF0Q2x6jh3RMBLcGuB93q2qL7VuKx89Y2c'
MSG = 'Are u programming today????? Go for it now, {}!!!!'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)  # Диспетчер, привязанный к боту

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):  # В эту функцию записываем основную логику приветствия пользователя. Причем функция асинхронная, тк используем асинхронную бибилиотеку aiogram
    user_id = message.from_user.id          # Из сообщения пользователя получаем данные о user_id
    user_full_name = message.from_user.full_name   # Из сообщения пользователя получаем данные о полном имени пользователя (user_full_name)
    user_name = message.from_user.first_name # Из сообщения получаем данные об имени пользователя
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')  # Уровень логирования INFO, в него передаем логирование user_id, user_full_name и текущее время
    await message.reply(f'Hello, {user_full_name}!') # Конструкция используется для ответа пользователя посредством message.reply

    for i in range(7):  # Цикл для создания лага, который будет отправляться через определенное время
        time.sleep(60*60*12)
        await bot.send_message(user_id, MSG.format(user_name))  # Конструкция отправляет с помощью бота сообщение пользователю MSG, в котором присутствует имя пользователя


if __name__ == '__main__':
    executor.start_polling(dp)  # С помощью экзекьтора начинаем пулить бота в сеть
