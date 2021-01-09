import logging

from loader import redis

user_prefix = "user_"


async def is_user(user_id: int) -> bool:
    is_user_exist = await redis.get(user_prefix + str(user_id))
    logging.info(f"---User {user_id} exist --- {is_user_exist} ---")
    return is_user_exist


async def set_new_user(user_id: int):
    out = await redis.set(user_prefix + str(user_id), "True")
    logging.info(f"---Set user {user_id} to redis_db---")


async def del_user(user_id: int):
    await redis.brpop(user_prefix + str(user_id))
    logging.info(f"---Del user {user_id} to redis_db---")

