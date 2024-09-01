from dataclasses import dataclass

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from environs import Env

wallet_name = 'wallet'
pause_time = 120

@dataclass
class TgBot:
    token: str
    admin_id: str
    drop_amount: str
    fee: str
    network: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN"),
                               admin_id=env("ADMIN_ID"),
                               drop_amount=env("DROP_AMOUNT"),
                               fee=env("FEE"),
                               network=env("NETWORK")))


config: Config = load_config()

token = config.tg_bot.token
admin_id = int(config.tg_bot.admin_id)
drop_amount = int(config.tg_bot.drop_amount)
fee = int(config.tg_bot.fee)
network = config.tg_bot.network

bot = Bot(token, default=DefaultBotProperties(parse_mode='HTML'))

