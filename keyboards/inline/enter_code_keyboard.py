from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

enter_code_callback = CallbackData("enter_code", "state")

enter_code_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Ввести реферальный код", callback_data=enter_code_callback.new(state="ok"))]
    ]
)