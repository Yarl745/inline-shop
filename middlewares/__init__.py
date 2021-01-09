from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .get_user import GetUserMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    # dp.middleware.setup(GetUserMiddleware())
