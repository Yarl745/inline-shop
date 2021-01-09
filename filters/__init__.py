from aiogram import Dispatcher


from .admin_filter import IsAdmin
from .user_filter import IsUser


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsUser)
    pass
