from typing import List

from aiogram import types
from sqlalchemy import or_

from utils.db_api.models import Item, User


async def add_item(**kwargs) -> Item:
    new_item = await Item(**kwargs).create()
    return new_item


async def search_items(text: str) -> List[Item]:
    if text:
        text = f"%{' '.join(text.split())}%"
        conditions = [Item.name.ilike(text), Item.description.ilike(text)]
    else:
        conditions = []
    return await Item.query.where(or_(*conditions)).order_by(Item.name).gino.all()


async def get_item(id: int) -> Item:
    return await Item.query.where(Item.id == id).gino.first()


async def add_user(**kwargs) -> User:
    new_user = await User(**kwargs).create()
    return new_user


async def get_referrals() -> List[User]:
    user_id = types.User.get_current().id
    referrals = await User.query.where(User.referral == user_id).gino.all()
    return referrals


async def get_user(user_id: int) -> User:
    return await User.query.where(User.user_id == user_id).gino.first()