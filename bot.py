import asyncio

from aiogram import Dispatcher

from config_data.config import admin_id, drop_amount, fee, bot
from handlers import admin_handlers, drop_handler, user_handler


async def main():
    dp = Dispatcher()

    await bot.send_message(chat_id=admin_id, text='tbtc_faucet-бот перезапущен\n'
                                                  f'сумма дропа = {drop_amount} sat\n'
                                                  f'комиссия = {fee} sat')

    dp.include_routers(user_handler.router, admin_handlers.router,
                       drop_handler.router)

    await dp.start_polling(bot, polling_timeout=30)


if __name__ == '__main__':
    asyncio.run(main())
