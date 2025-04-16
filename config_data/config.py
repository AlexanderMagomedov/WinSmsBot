from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class TgBot:
    token: str   # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    number_LK1: str
    number_LK2: str
    number_LK3: str
    number_LK4: str
    number_LK5: str
    number_LK6: str
    token_LK1: str
    token_LK2: str
    token_LK3: str
    token_LK4: str
    token_LK5: str
    token_LK6: str
    access_list: list
    mtt_url_balance: str
    mtt_url_count: str
    mtt_login: str
    mtt_password: str
    my_url: str
    my_key: str




def load_config() -> Config:
    return Config(tg_bot=TgBot(token=os.getenv('BOT_TOKEN')),
                  number_LK1=os.getenv('NUMBER_LK1'),
                  number_LK2=os.getenv('NUMBER_LK2'),
                  number_LK3=os.getenv('NUMBER_LK3'),
                  number_LK4=os.getenv('NUMBER_LK4'),
                  number_LK5=os.getenv('NUMBER_LK5'),
                  number_LK6=os.getenv('NUMBER_LK6'),
                  token_LK1=os.getenv('TOKEN_LK1'),
                  token_LK2=os.getenv('TOKEN_LK2'),
                  token_LK3=os.getenv('TOKEN_LK3'),
                  token_LK4=os.getenv('TOKEN_LK4'),
                  token_LK5=os.getenv('TOKEN_LK5'),
                  token_LK6=os.getenv('TOKEN_LK6'),
                  access_list=list(os.getenv('ACCESS_LIST').split(',')),
                  mtt_url_balance=os.getenv('MTT_URL_BALANCE'),
                  mtt_url_count=os.getenv('MTT_URL_COUNT'),
                  mtt_login=os.getenv('MTT_LOGIN'),
                  mtt_password=os.getenv('MTT_PASSWORD'),
                  my_url=os.getenv('MY_URL'),
                  my_key=os.getenv('MY_KEY'),
                  )
