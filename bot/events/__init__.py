from aiogram import Router


from .startup import router as startup_router
from .shutdown import router as shutdown_router


router = Router()

router.include_router(startup_router)
router.include_router(shutdown_router)