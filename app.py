import asyncio

from aiohttp import web

from utils.db_api.database import create_db
from utils.misc.payment_callbacks import listen_fondy_callbacks
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    await set_default_commands(dp)

    await create_db()

# async def on_shutdown(dp):
#     from loader import redis
#     redis.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

