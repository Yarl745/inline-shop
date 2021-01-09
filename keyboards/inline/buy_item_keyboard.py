from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

buy_item_callback = CallbackData("buy_item", "state")

buy_item_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", callback_data=buy_item_callback.new(state="ok"))],
    ]
)
