from aiogram import Router
from aiogram.filters import CommandStart


router = Router()

@router.shutdown()
async def on_shutdown() -> None:
    print("Bot is shutting down...")