from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

share_phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Поделится номером аккаунта📞", request_contact=True)]
    ],
    resize_keyboard=True
)