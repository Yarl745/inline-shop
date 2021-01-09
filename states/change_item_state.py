from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeItemState(StatesGroup):
	change_name = State()
	change_description = State()
	change_price = State()
	change_photo = State()
