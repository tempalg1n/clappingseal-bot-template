import structlog
from aiogram import Bot
from aiogram.exceptions import (TelegramBadRequest, TelegramForbiddenError,
                                TelegramRetryAfter)
from aiogram.types import InlineKeyboardButton, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dishka.integrations.base import FromDishka
from dishka.integrations.faststream import inject

from faststream.rabbit import RabbitMessage, RabbitRouter
from src.bot.structures.schemas.mail import TelegramMessage
from src.db import Database

AMQPMailingController = RabbitRouter()

logger = structlog.get_logger()


@AMQPMailingController.subscriber('mailing_queue', no_ack=True)
@inject
async def handle_mail(
        mail: TelegramMessage,
        db: FromDishka[Database],
        bot: FromDishka[Bot],
        msg: RabbitMessage,
) -> None:
    try:
        reply_markup = None

        if mail.button:
            button_kwargs = {"text": mail.button.text}
            if mail.button.url:
                button_kwargs["url"] = mail.button.url

            reply_markup = InlineKeyboardBuilder().add(
                InlineKeyboardButton(**button_kwargs)
            ).as_markup()
        if mail.image:
            photo = URLInputFile(url=mail.image.url, filename=mail.image.name)
            await bot.send_photo(mail.chat_id, photo=photo, caption=mail.message_text, reply_markup=reply_markup)
        else:
            await bot.send_message(mail.chat_id, mail.message_text, reply_markup=reply_markup)
        await msg.ack()

    except TelegramRetryAfter:
        await msg.nack()
        logger.warning(
            f"Rate limit exceeded: message '{mail.message_text}' not sent to user ID {mail.chat_id}."
        )
    except TelegramBadRequest as br:
        await msg.ack()
        logger.error(f"Telegram bad request: {br}")
    except TelegramForbiddenError as fb:
        await msg.ack()
        logger.error(f"Perhaps user blocked bot: {fb}")
    except Exception as e:
        await msg.ack()
        logger.critical(f"Unexpected exception! Failed to send message to user ID {mail.chat_id}. {e}")
