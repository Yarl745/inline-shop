from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentTypes
from aiogram.utils.markdown import hbold

from keyboards.default import cancel_keyboard, share_phone_keyboard
from keyboards.inline import buy_item_keyboard
from keyboards.inline.buy_item_keyboard import buy_item_callback
from keyboards.inline.pay_for_item_keyboard import get_pay_for_item_keyboard, pay_for_item_callback
from loader import dp
from states import BuyItemState
from utils.db_api import redis_commands, db_commands
from utils.db_api.models import Item
from utils.misc.payment import get_payment_info, get_payment_status


@dp.callback_query_handler(buy_item_callback.filter())
async def start_buy_item(call: CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()

    await call.message.answer("Введите количество товара:", reply_markup=cancel_keyboard)

    await BuyItemState.enter_amount.set()


@dp.message_handler(state=BuyItemState.enter_amount)
async def set_item_amount(message: types.Message, state: FSMContext):
    try:
        item_amount = int(message.text)
    except ValueError:
        await message.answer("Количество товаров должно быть целым числом!\n"
                             "Попробуйте ввести ещё раз:")
        return

    await state.update_data(item_amount=item_amount)

    await message.answer("Введите свой номер или поделитесь номером телефона вашего аккаунта телеграм, "
                         "для того чтоюы мы смогли связаться с вами:",
                         reply_markup=share_phone_keyboard)

    await BuyItemState.enter_phone.set()


@dp.message_handler(state=BuyItemState.enter_phone, content_types=ContentTypes.TEXT | ContentTypes.CONTACT)
async def set_user_phone(message: types.Message, state: FSMContext):
    user_phone = message.contact.phone_number if message.contact else message.text

    await state.update_data(user_phone=user_phone)

    await message.answer("Введите информацию по доставке(название своего города,"
                         " № отделения Новой почты, ваши предпочтения по доставке):",
                         reply_markup=cancel_keyboard)

    await BuyItemState.enter_shipping_info.set()


@dp.message_handler(state=BuyItemState.enter_shipping_info)
async def set_shipping_info(message: types.Message, state: FSMContext):
    shipping_info = message.text

    async with state.proxy() as data:
        user_phone = data.get('user_phone')
        amount = int(data.get('item_amount'))
        item_id = data.get('item_id')

    item = await db_commands.get_item(item_id)

    payment_info = await get_payment_info(amount * item.price)
    payment_url = payment_info.get('checkout_url')
    order_id = payment_info.get('order_id')

    await state.update_data(shipping_info=shipping_info,
                            order_id=order_id)

    buy_info_text = get_buy_info_text(user_phone, amount, shipping_info, item)

    await message.answer_photo(
        photo=item.photo_id,
        caption=buy_info_text,
        reply_markup=get_pay_for_item_keyboard(payment_url)
    )


def get_buy_info_text(user_phone: str, amount: int, shipping_info, item: Item):
    return f"{hbold('Стоимость: ')} {item.name} x {amount} = {amount*item.price}грн\n\n" \
           f"{hbold('Ваш номер телефона')}: {user_phone}\n\n" \
           f"{hbold('Информация по доставке')}: {shipping_info}"
