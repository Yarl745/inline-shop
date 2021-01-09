from io import BytesIO

from aiogram.types import PhotoSize

from loader import telegraph


async def get_image_link(photo: PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        links = await telegraph.upload(file)
    return links[0]