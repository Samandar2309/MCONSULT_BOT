"""
Middleware для добавления Bot'а в контекст
"""
from typing import Callable, Any, Awaitable
from aiogram import BaseMiddleware, Bot
from aiogram.types import Update


class BotMiddleware(BaseMiddleware):
    """Добавляет объект Bot'а в контекст всех обработчиков"""

    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ) -> Any:
        # Добавляем бота в data, чтобы обработчики могли его получить
        data["bot"] = self.bot
        return await handler(event, data)

