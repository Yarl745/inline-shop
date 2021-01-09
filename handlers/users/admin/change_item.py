from decimal import Decimal

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentTypes, InputMediaPhoto

from handlers.users.admin.add_item import get_item_text
from keyboards.inline.confirm_item_keyboard import change_item_callback, ITEM_NAME, ITEM_DESCRIPTION, ITEM_PRICE, \
    ITEM_PHOTO_ID
from loader import dp, bot
from states.add_item_state import AddItemState
from states.change_item_state import ChangeItemState
from utils.misc import get_image_link


@dp.callback_query_handler(change_item_callback.filter(), state=AddItemState.confirm_item, run_task=True)
async def change_item(call: CallbackQuery, state: FSMContext, callback_data: dict):
    component = callback_data["component"]
    message = call.message
    if component == ITEM_NAME:
        text = "Введите название товара:"
        await ChangeItemState.change_name.set()
    elif component == ITEM_DESCRIPTION:
        text = "Введите описание товара:"
        await ChangeItemState.change_description.set()
    elif component == ITEM_PRICE:
        text = "Введите цену товара:"
        await ChangeItemState.change_price.set()
    elif component == ITEM_PHOTO_ID:
        text = "Загрузите фото для товара:"
        await ChangeItemState.change_photo.set()

    last_msg_id = (await message.answer(text=text)).message_id
    await state.update_data(last_msg_id=last_msg_id)

    await call.answer()


@dp.message_handler(state=ChangeItemState.change_name)
async def change_item_name(message: types.Message, state: FSMContext):
    item_name = message.text

    async with state.proxy() as data:
        data['item_name'] = item_name
        item_description = data['item_description']
        item_price = data['item_price']
        item_msg_id = data['item_msg_id']
        last_msg_id = data['last_msg_id']

    item_text = get_item_text(item_name, item_description, item_price)

    await dp.bot.delete_message(message.chat.id, last_msg_id)
    await dp.bot.delete_message(message.chat.id, message.message_id)

    await dp.bot.edit_message_caption(message.chat.id, item_msg_id, caption=item_text)

    await AddItemState.confirm_item.set()


@dp.message_handler(state=ChangeItemState.change_description)
async def change_item_description(message: types.Message, state: FSMContext):
    item_description = message.html_text

    async with state.proxy() as data:
        data['item_description'] = item_description
        item_name = data['item_name']
        item_price = data['item_price']
        item_msg_id = data['item_msg_id']
        last_msg_id = data['last_msg_id']

    item_text = get_item_text(item_name, item_description, item_price)

    await dp.bot.delete_message(message.chat.id, last_msg_id)
    await dp.bot.delete_message(message.chat.id, message.message_id)

    await dp.bot.edit_message_caption(message.chat.id, item_msg_id, caption=item_text)

    await AddItemState.confirm_item.set()


@dp.message_handler(state=ChangeItemState.change_price)
async def change_item_price(message: types.Message, state: FSMContext):
    try:
        item_price = str(Decimal(message.text))
    except ValueError:
        await message.answer("Цена должна быть целым числом")
        return

    async with state.proxy() as data:
        data['item_price'] = item_price
        item_name = data['item_name']
        item_description = data['item_description']
        item_msg_id = data['item_msg_id']
        last_msg_id = data['last_msg_id']

    item_text = get_item_text(item_name, item_description, item_price)

    await dp.bot.delete_message(message.chat.id, last_msg_id)
    await dp.bot.delete_message(message.chat.id, message.message_id)

    await dp.bot.edit_message_caption(message.chat.id, item_msg_id, caption=item_text)

    await AddItemState.confirm_item.set()


@dp.message_handler(state=ChangeItemState.change_photo, content_types=ContentTypes.PHOTO)
async def change_item_photo(message: types.Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, 'upload_photo')

    item_photo_id = message.photo[-1].file_id
    item_small_photo = await get_image_link(message.photo[0])

    async with state.proxy() as data:
        data['item_photo_id'] = item_photo_id
        data['item_small_photo'] = item_small_photo
        item_price = data['item_price']
        item_name = data['item_name']
        item_description = data['item_description']
        item_msg_id = data['item_msg_id']
        last_msg_id = data['last_msg_id']

    item_text = get_item_text(item_name, item_description, item_price)

    await dp.bot.delete_message(message.chat.id, last_msg_id)
    await dp.bot.delete_message(message.chat.id, message.message_id)

    await dp.bot.edit_message_media(InputMediaPhoto(item_photo_id, item_text), message.chat.id, item_msg_id)

    await AddItemState.confirm_item.set()
