from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from config_data.config import load_config

config = load_config('./.env')
bot_token = config.tg_bot.token    # Сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_2: KeyboardButton = KeyboardButton(text='Огурцов 🥒')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]],
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start" и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=keyboard)


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(Text(text='Собак 🦮'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?')


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(Text(text='Огурцов 🥒'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки боятся больше')


if __name__ == '__main__':
    dp.run_polling(bot)
