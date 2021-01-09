from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query_handler(state="*")
async def default_answer(call: CallbackQuery):
    await call.answer()


# @dp.message_handler()
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
