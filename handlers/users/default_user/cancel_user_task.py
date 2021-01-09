from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsUser
from keyboards.default.cancel_keyboard import CANCEL_TASK
from keyboards.inline import show_items_keyboard
from loader import dp


@dp.message_handler(IsUser(), text=CANCEL_TASK, state="*")
async def cancel_user_task(message: types.Message, state: FSMContext):
    await state.finish()

    await message.answer(text="Отменено❌")

    await message.answer(
        text="Ищите другие товары в нашем магазине:",
        reply_markup=show_items_keyboard
    )