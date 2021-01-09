from aiogram.dispatcher.filters.state import StatesGroup, State


class AddItemState(StatesGroup):
	add_name = State()
	add_description = State()
	add_price = State()
	add_photo = State()
	confirm_item = State()