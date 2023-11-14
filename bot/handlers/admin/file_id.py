from typing import Any, Final

from aiogram import Router, F
from aiogram.methods import TelegramMethod
from aiogram.types import Message


router: Final[Router] = Router(name=__name__)


@router.message(F.document)
async def document_file_id(message: Message) -> TelegramMethod[Any]:
    return message.answer(message.document.file_id)


@router.message(F.photo)
async def photo_file_id(message: Message) -> TelegramMethod[Any]:
    return message.answer(message.photo[-1].file_id)


@router.message(F.video)
async def video_id(message: Message) -> TelegramMethod[Any]:
    return message.answer(message.video.file_id)
