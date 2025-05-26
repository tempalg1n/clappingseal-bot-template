"""This file represents a commands logic."""

from aiogram import Router, types
from aiogram.filters import CommandStart
from dishka import FromDishka
from dishka.integrations.aiogram import inject
from src.db import Database
from src.db.models import User
from aiogram.fsm.context import FSMContext


commands_handler_router = Router(name='commands')


@commands_handler_router.message(CommandStart())
@inject
async def start_handler(message: types.Message, state: FSMContext, user: FromDishka[User], db: FromDishka[Database]):
    """Start command handler."""
    await state.clear()
    if not user:
        await db.user.new(
            user_id=message.from_user.id,
            user_name=message.from_user.username,
            first_name=message.from_user.first_name,
            second_name=message.from_user.last_name
        )
        await db.session.commit()
    await message.answer("Hello, world!")