import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from faststream import FastStream
from src.bot.app import get_dp, get_bot
from src.faststream.app import get_faststream_app
from src.ioc import container


async def get_app():
    bot = await get_bot()
    faststream_app: FastStream = get_faststream_app()
    bot_dp: Dispatcher = get_dp()
    bot_dp.startup.register(faststream_app.broker.start)
    bot_dp.shutdown.register(faststream_app.broker.close)
    try:
        await bot_dp.start_polling(
            bot,
            allowed_updates=bot_dp.resolve_used_update_types(),
        )
    finally:
        await container.close()
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(get_app())