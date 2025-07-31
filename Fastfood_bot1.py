# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils import executor
#
# TOKEN = '7595382038:AAET7Dmx7njzMIbOTvyWIqCY0U0y1A18y_Q'  # Вставь сюда токен от BotFather
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# # Главное меню
# menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# menu_keyboard.add(KeyboardButton("🍔 Бургер"), KeyboardButton("🍕 Пицца"), KeyboardButton("🍟 Картошка"))
#
# # Хранилище заказов
# user_orders = {}
#
# dp.message.register(start_cmd,Command('start'))
# async def start_cmd(message: types.Message):
#     await message.answer("Добро пожаловать в FastFoodBot! 🍽️\nВыберите, что хотите заказать:", reply_markup=menu_keyboard)
#
# @dp.message_handler(lambda message: message.text in ["🍔 Бургер", "🍕 Пицца", "🍟 Картошка"])
# async def choose_food(message: types.Message):
#     user_orders[message.from_user.id] = {"item": message.text}
#     await message.answer("Теперь отправьте, пожалуйста, ваш адрес доставки 📍")
#
# @dp.message_handler(lambda message: message.from_user.id in user_orders and "address" not in user_orders[message.from_user.id])
# async def get_address(message: types.Message):
#     user_orders[message.from_user.id]["address"] = message.text
#     item = user_orders[message.from_user.id]["item"]
#     address = user_orders[message.from_user.id]["address"]
#     await message.answer(f"Ваш заказ: {item}\nАдрес доставки: {address}\nСпасибо за заказ! 🚀")
#     # Очистим заказ
#     user_orders.pop(message.from_user.id)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)












