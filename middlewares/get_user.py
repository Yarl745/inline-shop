from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api import db_commands


class GetUserMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user_id = types.User.get_current().id
        data['user'] = await db_commands.get_user(user_id)