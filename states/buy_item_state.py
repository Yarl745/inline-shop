from aiogram.dispatcher.filters.state import StatesGroup, State


class BuyItemState(StatesGroup):
    enter_amount = State()
    enter_phone = State()
    enter_shipping_info = State()
