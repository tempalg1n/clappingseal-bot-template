import datetime
import logging

import structlog
from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_aio_pika import AioPikaBroker
from src.bot.structures.schemas.mail import TelegramMailContent, TelegramMessage, ButtonSchema
from src.db.database import Database
from src.db.models.user import User
from dishka import FromDishka
from dishka.integrations.taskiq import inject
from faststream.rabbit import RabbitBroker
from faststream.rabbit.publisher.asyncapi import AsyncAPIPublisher

from src.taskiq_scheduler.broker import get_broker


logger = structlog.get_logger()

broker: AioPikaBroker = get_broker()
scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


# @broker.task(task_name='test_every_minute_message', schedule=[{"cron": "* * * * *"}])
# @inject
# async def test_every_minute_message(
#     rabbit: FromDishka[RabbitBroker]
# ):
#     mailing_publisher: AsyncAPIPublisher = rabbit.publisher('mailing_queue')
#     await mailing_publisher.publish(
#         TelegramMessage(
#             message_text="Test message",
#             chat_id=123807425,
#             mailing_id=1,
#             user_id=123807425,
#         )
#     )
#     logger.info('Test message sent to queue!')
