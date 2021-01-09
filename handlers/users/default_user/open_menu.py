from aiogram import types

from filters import IsUser
from keyboards.default.get_menu_keyboard import SHOW_GOODS
from keyboards.inline.show_items_keyboard import show_items_keyboard
from loader import dp


@dp.message_handler(IsUser(), text=SHOW_GOODS)
async def open_menu(message: types.Message):
    username = (await dp.bot.get_me()).username

    await message.answer(
        text="Вы сможете выбирать товары очень быстро. Для этого "
             f"нужно ввести @{username} в любом чате телеграм и вы сразу "
             f"сможете очуществлять поиск по товарам нашего магазина.\n\n"
             f"Попробуйте этот режим нажав на кнопку:",
        reply_markup=show_items_keyboard
    )
