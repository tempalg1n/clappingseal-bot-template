from dishka.integrations.taskiq import setup_dishka
from taskiq_aio_pika import AioPikaBroker
from src.ioc import taskiq_container
from src.configuration import conf

def get_broker(
    queue_name: str = 'taskiq_backend',
    exchange_name: str = 'taskiq_backend',
    routing_key: str = '#',
    qos: int = 10,
) -> AioPikaBroker:
    broker = AioPikaBroker(
        conf.rabbitmq.build_connection_str(),
        queue_name=queue_name,
        exchange_name=exchange_name,
        routing_key=routing_key,
        qos=qos,
    )
    setup_dishka(taskiq_container, broker)
    return broker