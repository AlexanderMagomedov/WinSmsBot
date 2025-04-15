from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

from startbot import config


class LK(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data in [config.number_LK1, config.number_LK2, config.number_LK3, config.number_LK4, config.number_LK5, config.number_LK6]

class Balance(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.split()[0] == '/B'

class Count_Number(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.split()[0] == '/C'