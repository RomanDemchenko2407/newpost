# from aiogram.types import Message
# from aiogram import Bot
# from aiogram import html
#
# async def bot_ishlasa(bot:Bot):
#     await bot.send_message(7469106857,"Бот начал работу✅")
#
#
# async def bot_tohtaganda(bot:Bot):
#     await bot.send_message(7469106857,"Бот завершил работу❌")
#
# async def start_bosganda(message:Message):
#     await message.answer(f"Здравствуйте! {html.bold(message.from_user.full_name)}")
#
# async def help_bosganda(message:Message):
#     await message.answer("Владельцем этого бота является @Bandits_3122")
#
# async def info_bosganda(message:Message, bot:Bot):
#     user= await bot.get_chat(message.from_user.id)
#     user_photos=await message.from_user.get_profile_photos()
#
#     malumotlar=f"""
# {message.from_user.first_name} Информация👇🏻
#
# ISM: {message.from_user.first_name}
# FAMILIYA:{message.from_user.last_name}
#
# """
#     if user.bio:
#         malumotlar+= f"BIO:{user.bio}"
#     if message.from_user.username:
#         malumotlar+= f"\nUSERNAME: @{message.from_user.username}"
#     if user_photos.photos:
#         user_chat_id= message.from_user.id
#         await bot.send_photo(chat_id=user_chat_id, photo=user_photos.photos[0][-1].file_id, caption=malumotlar)
#         await bot.send_photo(chat_id=7469106857, photo=user_photos.photos[0][-1].file_id, caption=malumotlar)
#     else:
#         user_chat_id = message.from_user.id
#         await bot.send_message(chat_id=user_chat_id, text=malumotlar)
#         await bot.send_message(chat_id=7469106857, text=malumotlar)
#
# async def calc_bosganda(message:Message):
#     try:
#         text=message.text
#         left_space=text.find(" ")
#         right_space=text.rfind(" ")
#         son1=int(text[:left_space])
#         amal=text[left_space+1 : right_space]
#         son2=int(text[right_space+1:])
#
#         if amal =="+":
#             result= f"{son1}+{son2}={son1+son2}"
#         elif amal =="-":
#             result= f"{son1}-{son2}={son1-son2}"
#         elif amal =="*":
#             result= f"{son1}*{son2}={son1*son2}"
#         elif amal ==":":
#             result= f"{son1}:{son2}={son1/son2}"
#
#         await message.answer(result, reply_to_message_id=message.message_id)
#     except:
#         await message.answer("Вы неправильно воспользовались калькулятором",reply_to_message_id=message.message_id)
#
