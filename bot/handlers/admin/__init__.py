from typing import Final

from aiogram import Router

from bot.filters import ADMIN_ONLY
from . import file_id

router: Final[Router] = Router(name=__name__)
router.include_router(file_id.router)
router.message.filter(ADMIN_ONLY)
router.callback_query.filter(ADMIN_ONLY)
