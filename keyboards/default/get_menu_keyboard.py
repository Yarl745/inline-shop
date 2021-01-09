from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

SHOW_GOODS = "Показать товары"

user_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(SHOW_GOODS)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)