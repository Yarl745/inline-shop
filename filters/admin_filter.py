from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery, Message, InlineQuery

from data.config import admins
from utils.db_api import redis_commands


class IsAdmin(BoundFilter):
    async def check(self, undefined, *args) -> bool:
        # Undefined can be Message, CallbackQuery and InlineQuery
        user_id = undefined.from_user.id
        return user_id in admins and await redis_commands.is_user(user_id)