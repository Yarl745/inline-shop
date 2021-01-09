from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

ITEM_NAME = 'item_name'
ITEM_DESCRIPTION = 'item_description'
ITEM_PRICE = 'item_price'
ITEM_PHOTO_ID = 'item_photo_id'

change_item_callback = CallbackData("change_item", "component")
confirm_item_callback = CallbackData("confirm_item_callback", "state")

confirm_item_keyboard = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton("Сохранить✅", callback_data=confirm_item_callback.new(state="ok"))],
		[InlineKeyboardButton("🛠Изменить🛠", callback_data="default")],
		[
			InlineKeyboardButton("Название", callback_data=change_item_callback.new(component=ITEM_NAME)),
			InlineKeyboardButton("Описание", callback_data=change_item_callback.new(component=ITEM_DESCRIPTION)),
			InlineKeyboardButton("Цену", callback_data=change_item_callback.new(component=ITEM_PRICE)),
			InlineKeyboardButton("Фото", callback_data=change_item_callback.new(component=ITEM_PHOTO_ID)),
		]
	]
)
