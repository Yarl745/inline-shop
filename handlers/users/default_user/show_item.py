import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import deep_linking

from filters import IsUser
from handlers.users.admin.add_item import get_item_text
from keyboards.inline import buy_item_keyboard
from loader import dp
from utils.db_api import db_commands
from utils.misc import logging


@dp.message_handler(CommandStart(deep_link=re.compile('.+')), IsUser())
async def show_item(message: types.Message, state: FSMContext):
    item_id = int(deep_linking.decode_payload(message.get_args()))
    item = await db_commands.get_item(item_id)

    await state.update_data(item_id=item_id)

    logging.info(f"Buy {item}")

    await message.answer_photo(
        photo=item.photo_id,
        caption=get_item_text(item.name, item.description, item.price),
        reply_markup=buy_item_keyboard
    )


