import logging
from typing import AsyncIterable, AsyncIterator

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import TelegramObject, PollAnswer
from dishka import Provider, Scope, from_context, make_async_container, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from dishka.integrations.taskiq import TaskiqProvider
from faststream.rabbit import RabbitBroker


from src.configuration import Configuration, conf
from src.db.database import Database, new_session_maker
from src.db.models.user import User
from src.faststream.broker import new_broker

logger = logging.getLogger(__name__)


class AppProvider(Provider):
    config = provide(Configuration, scope=Scope.APP)
    telegram_object = from_context(provides=TelegramObject, scope=Scope.REQUEST)

    @provide(scope=Scope.REQUEST)
    async def get_bot(self, config: Configuration) -> AsyncIterable[Bot]:
        async with Bot(config.bot.token, default=DefaultBotProperties(parse_mode='HTML')) as bot:
            yield bot

    @provide(scope=Scope.APP)
    def get_session_maker(
            self, config: Configuration
    ) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(config.db)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    db = provide(Database, scope=Scope.REQUEST, provides=Database)

    @provide(scope=Scope.REQUEST)
    async def get_current_user(
            self,
            telegram_object: TelegramObject,
            db: Database,
    ) -> User:
        if isinstance(telegram_object, PollAnswer):
            user_id = telegram_object.user.id
        else:
            user_id = telegram_object.from_user.id

        user: User | None = await db.user.get_by_where(
            User.user_id == user_id
        )
        return user
    
    @provide(scope=Scope.REQUEST)
    async def get_broker(
        self, config: Configuration
    ) -> AsyncIterator[RabbitBroker]:
        async with new_broker(config.rabbitmq) as broker:
            yield broker


container = make_async_container(AppProvider(), context={Configuration: conf})
taskiq_container = make_async_container(
    AppProvider(), TaskiqProvider(), context={Configuration: conf}
)