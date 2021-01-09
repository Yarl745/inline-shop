import asyncio

from utils.db_api import db_commands
from utils.db_api.database import create_db


async def test():
    await create_db()

    await db_commands.add_item(
        name="Some name",
        description="Some Description",
        price=1000,
        photo="https://www.verywellfit.com/thmb/a4580FjTjbub9q4kI5m9X-Po-p0=/2002x1334/filters:no_upscale():max_bytes(150000):strip_icc()/Bananas-5c6a36a346e0fb0001f0e4a3.jpg"
    )
    await db_commands.add_item(
        name="some name with",
        description="dog and cat",
        price=20,
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwcWiO7BSv6xpwydMx08H68_7dQHMo4mwpkg&usqp=CAU"
    )
    await db_commands.add_item(
        name="apple",
        description="very expensive fruit",
        price=1000000000,
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkytcwzy84-WjcemOSlvUVcKHIRQVFMX6TEg&usqp=CAU"
    )
    await db_commands.add_item(
        name="aobeme",
        description="CHECK THIS TEXT",
        price=50,
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzTJKmDoTZNw7GzHfX_b77fvd5qcCa1mgL1w&usqp=CAU"
    )

    print(await db_commands.get_item(1), '\n'*5)

    print(await db_commands.search_items(""), '\n'*5)
    print(await db_commands.search_items("some"), '\n'*5)
    print(await db_commands.search_items("dog and"), '\n'*5)
    print(await db_commands.search_items("Expensive"), '\n'*5)
    print(await db_commands.search_items("aob"), '\n'*5)
    print(await db_commands.search_items("SOME       "), '\n'*5)



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(test())
