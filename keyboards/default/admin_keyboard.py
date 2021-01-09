from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ADD_ITEM = "Добавить товар"
COUNT_USERS = "Кол-во пользователей"
PURCHASES = "Заказы"
SHOW_DB = "База товаров"

admin_keyboard = ReplyKeyboardMarkup(keyboard=[
	[
		KeyboardButton(ADD_ITEM),
		KeyboardButton(PURCHASES)
	],
	[
		KeyboardButton(COUNT_USERS),
		KeyboardButton(SHOW_DB)
	]
], resize_keyboard=True)