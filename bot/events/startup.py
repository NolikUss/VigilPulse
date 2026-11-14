from aiogram import Router
from aiogram.filters import CommandStart


router = Router()

@router.startup()
async def on_startup() -> None:
    print("Bot is starting...")