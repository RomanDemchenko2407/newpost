# import asyncio
# from aiogram import Dispatcher, Bot, html
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from Telegram_bot2 import (bot_ishlasa,
#                            bot_tohtaganda,
#                            start_bosganda,
#                            help_bosganda,
#                            info_bosganda,
#                            calc_bosganda)
# from aiogram.types import BotCommand
# from aiogram.filters import Command
#
#
#
# TOKEN="7771116762:AAGDcQ76TqDLrxkH0-EJvMhEmBwHByZSfAc"
# dp= Dispatcher()
#
#
#
# async def main():
#     dp.startup.register(bot_ishlasa)
#     dp.message.register(start_bosganda,Command('start'))
#     dp.message.register(help_bosganda,Command('help'))
#     dp.message.register(info_bosganda,Command('info'))
#     dp.message.register(calc_bosganda)
#     bot=Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     dp.shutdown.register(bot_tohtaganda)
#     await bot.set_my_commands([
#         BotCommand(command="/start", description="Чтобы запустить бота..."),
#         BotCommand(command="/help", description="Полезная информация..."),
#         BotCommand(command="/info", description="Информация о вас..."),
#     ])
#     await dp.start_polling(bot)
#
# asyncio.run(main())
