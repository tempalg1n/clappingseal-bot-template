"""This package is used for a bot logic implementation."""
from src.bot.logic.handlers.commands import commands_handler_router

routers = (
    commands_handler_router,
)
