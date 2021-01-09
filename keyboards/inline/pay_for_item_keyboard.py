from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.misc.payment import get_payment_info

pay_for_item_callback = CallbackData("pay_for_item", "status")


def get_pay_for_item_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Оплатить💵", url=url, callback_data=pay_for_item_callback.new(status='OK'))
            ]
        ]
    )
