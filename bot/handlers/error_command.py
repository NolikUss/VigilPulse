from aiogram import F
from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(F.text.startswith("/"))
async def unknown_command(message: Message):
    await message.answer("❌ Unknown command.")