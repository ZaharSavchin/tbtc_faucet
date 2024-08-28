from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer('Бот для получения бесплатных bitcoin в сети testnet.\n'
                         'ДАННЫЕ МОНЕТЫ НЕ ИМЕЮТ НИКАКОЙ ЦЕННОСТИ И ПРЕДНАЗНАЧЕНЫ ТОЛЬКО ДЛЯ ТЕСТИРОВАНИЯ ПРИЛОЖЕНИЙ.\n'
                         'Просто отправьте боту адрес своего кошелька в сети testnet.\n'
                         'Для получения своего адреса запустите bitcoin-core или electrum из терминала с параметром --testnet')