from operator import index

from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery
import aiohttp

from filters.filters import LK, Balance, Count_Number
from keyboards.keyboards import create_menu_keyboard, create_lk_menu, create_back_to_lk, create_other_keyboard, \
    create_back_to_other
from lexicon.lexicon_ru import LEXICON
from startbot import config


router = Router()


# Эт X срабатывает на команду "/start" отправлять приветственное сообщение показывая кнопки главного меню
@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    if str(message.from_user.username)  in config.access_list:
        await message.answer(LEXICON['main_menu'], reply_markup=create_menu_keyboard())
    else:
        await message.answer(LEXICON['no_access'])
    await message.delete()


# Эт X срабатывает на нажатие инлайн-кнопки "Назад" и возвращать в главное меню
@router.callback_query(F.data == '/start')
async def process_start(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON['main_menu'], reply_markup=create_menu_keyboard())
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки с номером ЛК
@router.callback_query(LK())
async def process_lk_menu(callback: CallbackQuery):
    if callback.data == f'{config.number_LK1}':
        await callback.message.edit_text(
            text=f'Вы находитесь в меню ЛК №{config.number_LK1} Дмитрий',
            reply_markup=create_lk_menu(config.number_LK1))
    elif callback.data == f'{config.number_LK2}':
        await callback.message.edit_text(
            text = f'Вы находитесь в меню ЛК №{config.number_LK2} SmsHub (СХ)',
            reply_markup = create_lk_menu(config.number_LK2))
    elif callback.data == f'{config.number_LK3}':
        await callback.message.edit_text(
            text = f'Вы находитесь в меню ЛК №{config.number_LK3} uForce',
            reply_markup = create_lk_menu(config.number_LK3))
    elif callback.data == f'{config.number_LK4}':
        await callback.message.edit_text(
            text = f'Вы находитесь в меню ЛК №{config.number_LK4} Sigma (Давид)',
            reply_markup = create_lk_menu(config.number_LK4))
    elif callback.data == f'{config.number_LK5}':
        await callback.message.edit_text(
            text = f'Вы находитесь в меню ЛК №{config.number_LK5} Вебит',
            reply_markup = create_lk_menu(config.number_LK5))
    elif callback.data == f'{config.number_LK6}':
        await callback.message.edit_text(
            text = f'Вы находитесь в меню ЛК №{config.number_LK6} Леонид',
            reply_markup = create_lk_menu(config.number_LK6))
    await callback.answer()

# Эт X срабатывает на нажатие инлайн-кнопки "Баланс личного кабинета"
@router.callback_query(Balance())
async def process_lk_balance(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Баланс ЛК №{callback.data.split()[1]} \n'
             f'real_balance = {await mtt_request(callback.data.split()[1])}',
        reply_markup=create_back_to_lk(callback.data.split()[1]))
    await callback.answer()

#Функция получения баланса MTT
async def mtt_request(LK) -> str:
    login = config.mtt_login
    password = config.mtt_password
    url = config.mtt_url_balance
    data = {"jsonrpc":"2.0","method":"getCustomerBalance","params":[f"{LK}"],"id":1}

    auth = aiohttp.BasicAuth(login, password)
    async with aiohttp.ClientSession(auth=auth) as session:
        async with session.post(url, json=data) as response:
            if response.status != 200:
                return f"Сервис временно не доступен!!!"
            json_data = await response.json()
            return json_data.get("result", {}).get("real_balance")


# Эт X срабатывает на нажатие инлайн-кнопки "Баланс личного кабинета"
@router.callback_query(Count_Number())
async def process_lk_balance(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Количество номеров ЛК №{callback.data.split()[1]} \n'
             f'Номеров {await mtt_count_numbers(callback.data.split()[1])} шт.',
        reply_markup=create_back_to_lk(callback.data.split()[1]))
    await callback.answer()


async def mtt_count_numbers(LK) -> str:
    index = [config.number_LK1, config.number_LK2, config.number_LK3, config.number_LK4, config.number_LK5, config.number_LK6]
    token = [config.token_LK1, config.token_LK2, config.token_LK3, config.token_LK4, config.token_LK5, config.token_LK6][index.index(LK)]
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    url = config.mtt_url_count
    data = {"limit": 5000,"offset":0}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data) as response:
            if response.status != 200:
                return f"Сервис временно не доступен!!!"
            json_data = await response.json()
            return json_data.get("total")

# Эт X срабатывает на нажатие инлайн-кнопки "Прочее"
@router.callback_query(F.data == '/other')
async def process_other(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON['other'], reply_markup=create_other_keyboard())
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "Кол-во номеров на СХ" и возвращать в главное меню
@router.callback_query(F.data == '/SH_Numbers')
async def process_sh_numbers(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Кол-во номеров на СХ {await my_request_numbers()} шт.',
                                     reply_markup=create_back_to_other())
    await callback.answer()



#Функция получения баланса MTT
async def my_request_numbers() -> str:
    url = config.my_url + '/internal_services/sms_hub/actions'
    data = {"action": "GET_SERVICES", "key": config.my_key}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status != 200:
                return f"Сервис временно не доступен!!!"
            json_data = await response.json()
            return json_data["countryList"][0]["operatorMap"]["mtt_virtual"]["apd"]
