from aiogram import Router
from aiogram.types import Message
from bitcoinlib.wallets import Wallet, WalletError

from config_data.config import drop_amount, fee, network, admin_id, bot, wallet_name

router = Router()


@router.message(lambda message: isinstance(message.text, str) and
                                ' ' not in message.text.strip())
async def send_drop(message: Message):
   try:
        wallet = Wallet(wallet_name)
        user, user_id = message.from_user.full_name, message.from_user.id
        wallet.utxos_update()
        tr = wallet.send_to(to_address=message.text, amount=drop_amount, fee=fee, network=network, offline=False)
        await message.answer(f'Хэш транзакции: {tr}\n'
                            f'можете проверить статус транзакции на сайте https://blockstream.info/testnet/')
        await bot.send_message(admin_id, f'проведена транзакция {tr}\n'
                                        f'на адрес {message.text}\n'
                                        f'пользователем {user}, {user_id}')
   except WalletError:
       await message.answer('извините, транзакция не удалась')
       await bot.send_message(admin_id, 'недостаточно средств для транзакции')
