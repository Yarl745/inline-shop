from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import admins
from filters.admin_filter import IsAdmin
from keyboards.default import cancel_keyboard
from keyboards.default.admin_keyboard import ADD_ITEM
from loader import dp
from states.add_item_state import AddItemState


@dp.message_handler(IsAdmin(), text=ADD_ITEM)
async def create_item(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer(text="Введите название товара:", reply_markup=cancel_keyboard)
	await AddItemState.add_name.set()


