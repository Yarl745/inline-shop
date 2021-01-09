from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsAdmin
from keyboards.default import admin_keyboard
from keyboards.default.cancel_keyboard import CANCEL_TASK
from loader import dp


@dp.message_handler(IsAdmin(), text=CANCEL_TASK, state="*")
async def cancel_task(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Возвращаемся в админ-меню...", reply_markup=admin_keyboard)
