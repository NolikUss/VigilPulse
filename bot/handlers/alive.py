from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("alive"))
async def alive(message: Message) -> None:
    await message.reply("I'm alive!")