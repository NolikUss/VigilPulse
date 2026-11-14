import logging

from aiogram import Router
from aiogram.filters import CommandStart


router = Router()
router = Router()
logger =  logging.getLogger(__name__)




@router.shutdown()
async def on_shutdown() -> None:
    logger.warning("Bot is shutting down...")