from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import admins
from filters import IsUser
from keyboards.default.admin_keyboard import admin_keyboard
from keyboards.default.get_menu_keyboard import user_menu_keyboard
from keyboards.inline.enter_code_keyboard import enter_code_keyboard
from loader import dp
from utils.db_api import redis_commands, db_commands


@dp.message_handler(CommandStart(), user_id=admins)
async def admin_bot_start(message: types.Message, state: FSMContext):
    await state.finish()

    await message.answer(f'Приветcтвую, дрогой админ {message.from_user.full_name}!',
                         reply_markup=admin_keyboard)

    if not await redis_commands.is_user(message.from_user.id):
        user = message.from_user
        await db_commands.add_user(
            user_id=user.id,
            username=user.username,
            full_name=user.full_name,
        )
        await redis_commands.set_new_user(message.from_user.id)


@dp.message_handler(CommandStart(), IsUser())
async def user_bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}, мы тебя помним.\n"
                         f"Ты можешь пользоваться этим магазиом использовав меню снизу⬇️",
                         reply_markup=user_menu_keyboard)


@dp.message_handler(CommandStart())
async def default_bot_start(message: types.Message, state: FSMContext):
    await message.answer(
        f"Здравствуйте, вы не можете пользоваться магазином,"
        f"так как вы не являетесь нашим пользователем😔\n\n"
        f"Попросите вашего друга поделиться с вами реферальной ссылкой "
        f"или введите реферальный код!",
        reply_markup=enter_code_keyboard
    )