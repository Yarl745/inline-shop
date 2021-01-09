from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, InlineQuery

from utils.db_api import redis_commands


class IsUser(BoundFilter):
    async def check(self, undefined, *args) -> bool:
        # Undefined can be Message, CallbackQuery and InlineQuery
        user_id = undefined.from_user.id
        return await redis_commands.is_user(user_id)