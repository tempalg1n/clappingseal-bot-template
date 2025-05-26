"""This file represent startup bot logic."""
import asyncio
import logging
import sys

import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from dishka.integrations.aiogram import setup_dishka
from redis.asyncio.client import Redis

from src.bot.dispatcher import get_redis_storage, setup_dispatcher
from src.configuration import conf
from src.ioc import container

logger = structlog.get_logger()

COMMANDS = {
    'start': 'Рестарт',
}


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command,
    description in COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)


def get_dp() -> Dispatcher:

    storage = get_redis_storage(
        redis=Redis(
            db=conf.redis.db,
            host=conf.redis.host,
            password=conf.redis.passwd,
            username=conf.redis.username,
            port=conf.redis.port,
        )
    )
    dp = setup_dispatcher(storage=storage)

    setup_dishka(container=container, router=dp)

    return dp


async def get_bot() -> Bot:
    bot = Bot(
        token=conf.bot.token, default=DefaultBotProperties(parse_mode='HTML')
    )
    await set_main_menu(bot)
    return Bot(
        token=conf.bot.token, default=DefaultBotProperties(parse_mode='HTML')
    )
