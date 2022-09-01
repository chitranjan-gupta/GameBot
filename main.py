from uuid import uuid4
from aiogram import *
import logging
import os
#from aiogram import Bot, Dispatcher,executor, types
from aiogram.types import InlineQueryResultGame
#from aiogram.handlers import CallbackQueryHandler
BOT_TOKEN = os.environ.get('token')
logging.basicConfig(level=logging.INFO)
url='https://examsforcareers.vercel.app'
game_short_name='Chitchat'
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

@disp.callback_query_handler()
async def send_welcome(callback_query: types.CallbackQuery):
  await bot.answer_callback_query(callback_query.id,url=url)

@disp.inline_handler()
async def send_game(inline_query: types.InlineQuery):
  await bot.answer_inline_query(inline_query.id,[InlineQueryResultGame(id=str(uuid4()),game_short_name=game_short_name)])

if __name__ == '__main__':
  executor.start_polling(disp)
