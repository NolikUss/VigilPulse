from aiogram import Router


from .alive import router as alive_router
from .error_command import router as error_router

router = Router()

router.include_router(alive_router)
router.include_router(error_router)