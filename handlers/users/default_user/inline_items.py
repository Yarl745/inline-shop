from typing import List

from aiogram.types import InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import deep_linking
from aiogram.utils.deep_linking import get_start_link

from filters import IsUser
from loader import dp, bot
from utils.db_api import db_commands
from utils.db_api.models import Item


@dp.inline_handler(IsUser())
async def show_searched_items(query: InlineQuery):
    query_text = query.query
    items = await db_commands.search_items(query_text)
    await query.answer(
        results=await get_results(items),
        cache_time=10
    )


async def get_results(items: List[Item]):
    results = []
    for item in items:
        results.append(
            InlineQueryResultArticle(
                id=item.id,
                title=item.name,
                description=f"Цена: {item.price}грн",
                thumb_url=item.small_photo,
                input_message_content=InputTextMessageContent(
                    message_text=f"Подробная информация про {item.name}"
                ),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton("Перейти", url=await get_start_link(str(item.id), encode=True))]
                    ]
                )
            )
        )
    return results


async def get_buy_link(item_id: str):
    encoded_item_id = deep_linking.encode_payload(item_id)
    bot_username = (await bot.get_me()).username
    return f"https://t.me/{bot_username}?buy={encoded_item_id}"

