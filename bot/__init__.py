from aiogram import Router

from .events import router as events_router
from .handlers import router as handlers_router

router = Router()

router.include_router(events_router)
router.include_router(handlers_router)