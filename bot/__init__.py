from aiogram import Router

from events.__init__ import router as events_router


router = Router()

router.include_router(events_router)