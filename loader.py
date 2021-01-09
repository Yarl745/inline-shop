import aioredis
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiograph import Telegraph
from aiohttp import web
from gino import Gino

from data import config
# from utils.db_api.database import db

from asgiref.sync import async_to_sync


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2(host='localhost')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

redis = async_to_sync(aioredis.create_redis_pool)('redis://localhost')

db = Gino()

telegraph = Telegraph()

__all__ = ["dp", "db", "bot", "redis"]
