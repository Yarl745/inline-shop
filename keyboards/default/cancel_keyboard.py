from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

CANCEL_TASK = "Отменить"

cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=CANCEL_TASK)]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)