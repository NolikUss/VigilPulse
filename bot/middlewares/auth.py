from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from bot.services.config import config


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user = getattr(event, "from_user", None)

        if user is None:
            return await handler(event, data)

        allowed_users = config["security"]["allowed_users"]

        if user.id not in allowed_users:
            if isinstance(event, Message):
                await event.answer("⛔ У вас нет доступа.")
            elif isinstance(event, CallbackQuery):
                await event.answer("⛔ У вас нет доступа.", show_alert=True)
            return

        return await handler(event, data)