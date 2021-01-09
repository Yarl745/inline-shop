from decimal import Decimal, InvalidOperation

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from keyboards.default.admin_keyboard import admin_keyboard
from keyboards.inline.confirm_item_keyboard import confirm_item_keyboard, confirm_item_callback
from loader import dp, bot
from states.add_item_state import AddItemState
from utils.db_api import db_commands
from utils.misc import get_image_link


@dp.message_handler(state=AddItemState.add_name)
async def add_item_name(message: types.Message, state: FSMContext):
    item_name = message.text
    async with state.proxy() as data:
        data['item_name'] = item_name
    await AddItemState.add_description.set()
    await message.answer("Введите описание товара:")


@dp.message_handler(state=AddItemState.add_description)
async def add_item_description(message: types.Message, state: FSMContext):
    item_description = message.html_text
    async with state.proxy() as data:
        data['item_description'] = item_description
    await AddItemState.add_price.set()
    await message.answer("Введите цену товара:")


@dp.message_handler(state=AddItemState.add_price)
async def add_item_price(message: types.Message, state: FSMContext):
    try:
        item_price = str(Decimal(message.text))
    except InvalidOperation:
        await message.answer("Цена должна быть целым числом")
        return

    async with state.proxy() as data:
        data['item_price'] = item_price
    await AddItemState.add_photo.set()
    await message.answer("Загрузите фото для товара:")


@dp.message_handler(state=AddItemState.add_photo, content_types=ContentTypes.PHOTO)
async def add_item_photo(message: types.Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, "upload_photo")

    data = await state.get_data()
    item_name = data['item_name']
    item_description = data['item_description']
    item_price = data['item_price']
    item_photo_id = message.photo[-1].file_id
    item_small_photo = await get_image_link(message.photo[0])

    item_text = get_item_text(item_name, item_description, item_price)

    item_msg_id = (await message.answer_photo(photo=item_photo_id, caption=item_text)).message_id

    await message.answer(text="Сохранить товар?", reply_markup=confirm_item_keyboard)

    async with state.proxy() as data:
        data['item_photo_id'] = item_photo_id
        data['item_small_photo'] = item_small_photo
        data['item_msg_id'] = item_msg_id

    await AddItemState.confirm_item.set()


@dp.callback_query_handler(confirm_item_callback.filter(), state=AddItemState.confirm_item)
async def save_item(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        item_name = data['item_name']
        item_description = data['item_description']
        item_price = Decimal(data['item_price'])
        item_photo_id = data['item_photo_id']
        item_small_photo = data['item_small_photo']

    await db_commands.add_item(name=item_name, description=item_description,
                               price=item_price, photo_id=item_photo_id,
                               small_photo=item_small_photo)

    await call.message.edit_text(text="Товар сохранён✅")
    await call.answer()

    await call.message.answer(text="Возвращаемся в меню", reply_markup=admin_keyboard)

    await state.finish()


def get_item_text(item_name, item_description, item_price):
    item_text = f"{hbold('Товар:')} {item_name}\n\n" \
                f"{hbold('Описание:')} {item_description}\n\n" \
                f"{hbold('Цена:')} {item_price}грн"
    return item_text
