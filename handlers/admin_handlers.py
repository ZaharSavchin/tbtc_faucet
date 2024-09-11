from bitcoinlib.wallets import WalletError
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bitcoinlib.wallets import Wallet

from config_data.config import admin_id, wallet_name, network, bot

router = Router()


@router.message(Command(commands='create_wallet'))
async def create_wallet(message: Message):
    if message.from_user.id == admin_id:
        wait_message = await message.answer('Подождите пожалуйста, соединение с сетью требует немного времени...')
        try:
            my_wallet = Wallet.create(wallet_name, network=network)
            address = my_wallet.addresslist()[0]
            await bot.send_message(admin_id, f'Создан кошелёк с адресом {address}')
            await wait_message.delete()
        except WalletError:
            wallet = Wallet(wallet_name)
            addr = wallet.addresslist()[0]
            await bot.send_message(admin_id, f'кошелек уже создан с адресом:\n'
                                             f'{addr}')
            await wait_message.delete()

@router.message(Command(commands='get_balance'))
async def get_balance(message: Message):
    if message.from_user.id == admin_id:
        wait_message = await message.answer('Подождите пожалуйста, соединение с сетью требует немного времени...')
        try:
            wallet = Wallet(wallet_name)
            wallet.utxos_update()
            balance = wallet.balance_update_from_serviceprovider()
            await bot.send_message(admin_id, f'{balance} sat (баланс обновляется после подтверждения транзакций в блокчейне сети)')
            await wait_message.delete()
        except WalletError:
            await bot.send_message(chat_id=admin_id, text='Кошелек не создан')
            await wait_message.delete()


@router.message(F.text == 'admin')
async def get_commands(message: Message):
    if message.from_user.id == admin_id:
        await message.answer('/create_wallet - создать кошелек\n'
                             '/get_balance - проверить баланс')
