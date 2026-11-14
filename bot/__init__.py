from aiogram import Router

from .events import router as events_router

router = Router()

router.include_router(events_router)