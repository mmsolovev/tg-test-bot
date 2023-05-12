from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import BotCommand, Message

from config_data.config import Config, load_config

# Создаем объект config
config: Config = load_config('./.env')

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)


@dp.message(Command(commands='delmenu'))
async def del_menu_command(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


if __name__ == '__main__':

    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)
