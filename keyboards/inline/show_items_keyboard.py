from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

show_items_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Показать товары", switch_inline_query_current_chat=" ")]
    ]
)
