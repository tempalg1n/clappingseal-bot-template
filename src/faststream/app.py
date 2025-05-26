from faststream import FastStream
from src.configuration import conf
from src.faststream.broker import new_broker
from src.faststream.handlers.mailing import AMQPMailingController
from src.ioc import container
from dishka.integrations import faststream as faststream_integration

import structlog

logger = structlog.get_logger()


def get_faststream_app() -> FastStream:
    broker = new_broker(conf.rabbitmq)
    faststream_app = FastStream(broker, logger=logger)

    faststream_integration.setup_dishka(
        container, faststream_app, auto_inject=True
    )
    broker.include_router(AMQPMailingController)
    return faststream_app
