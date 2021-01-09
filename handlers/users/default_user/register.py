from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ForceReply

from keyboards.default.get_menu_keyboard import user_menu_keyboard
from keyboards.inline.enter_code_keyboard import enter_code_callback
from loader import dp
from utils.db_api import redis_commands, db_commands


@dp.callback_query_handler(enter_code_callback.filter())
async def become_user(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    await call.message.answer(
        f"Посздравляю, {call.from_user.full_name}!\n"
        f"Теперь ты можешь пользоваться этим магазином🥳"
    )

    await call.message.answer(
        text=f"Ты можешь пользоваться этим магазиом использовав меню снизу⬇️",
        reply_markup=user_menu_keyboard
    )

    user = call.from_user
    await redis_commands.set_new_user(call.from_user.id)
    await db_commands.add_user(
        user_id=user.id,
        username=user.username,
        full_name=user.full_name
    )

    await call.answer()