from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON
from startbot import config


# Функция создания инлайн кнопок главного меню
def create_menu_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(
        InlineKeyboardButton(text=f'ЛК №{config.number_LK1} Дмитрий', callback_data=f'{config.number_LK1}'),
        InlineKeyboardButton(text=f'ЛК №{config.number_LK2} SmsHub (СХ)', callback_data=f'{config.number_LK2}'),
        InlineKeyboardButton(text=f'ЛК №{config.number_LK3} uForce', callback_data=f'{config.number_LK3}'),
        InlineKeyboardButton(text=f'ЛК №{config.number_LK4} Sigma (Давид)', callback_data=f'{config.number_LK4}'),
        InlineKeyboardButton(text=f'ЛК №{config.number_LK5} Вебит', callback_data=f'{config.number_LK5}'),
        InlineKeyboardButton(text=f'ЛК №{config.number_LK6} Леонид', callback_data=f'{config.number_LK6}'), width=1
    )
    return kb_builder.as_markup()


# Функция создания инлайн кнопок меню Личного кабинета
def create_lk_menu(number_LK) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(
        InlineKeyboardButton(text=f'Баланс личного кабинета', callback_data=f'/B {number_LK}'),
        InlineKeyboardButton(text=f'Количество номеров', callback_data=f'/C {number_LK}'), width=1
    )
    kb_builder.row(InlineKeyboardButton(text=LEXICON['/back'], callback_data='/start'))
    return kb_builder.as_markup()


# Функция создания инлайн кнопки назад в ЛК
def create_back_to_lk(number_LK) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(InlineKeyboardButton(text=LEXICON['/back'], callback_data=f'{number_LK}'))
    return kb_builder.as_markup()
