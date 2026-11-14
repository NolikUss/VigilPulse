import logging


from aiogram import Router
from aiogram.filters import CommandStart


router = Router()
logger =  logging.getLogger(__name__)


@router.startup()
async def on_startup() -> None:
    logger.warning("Bot is starting...")