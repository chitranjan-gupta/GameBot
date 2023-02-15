from uuid import uuid4
from aiogram import *
import logging
import os
#from aiogram import Bot, Dispatcher,executor, types
from aiogram.types import InlineQueryResultGame
#from aiogram.handlers import CallbackQueryHandler
BOT_TOKEN = os.environ.get('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
disp = Dispatcher(bot=bot)
@disp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  await message.reply("Hi!")

@disp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
  await message.reply("Type /start to Interact With The Bot")

@disp.message_handler()
async def echo(message: types.Message):
  print(message)
  await message.answer(message.text)

if __name__ == '__main__':
  executor.start_polling(disp)
