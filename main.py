import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from bot.services.logger import setup_logging
from bot.middlewares.auth import AuthMiddleware


# Events
from bot import router as main_router





async def main() -> None:
    load_dotenv()
    dp = Dispatcher()
    setup_logging()


    dp.include_router(main_router)
    dp.message.middleware(AuthMiddleware())
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise RuntimeError("BOT_TOKEN is not set. Add it to your .env file.")
    async with Bot(token=bot_token) as bot:
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
