from aiogram import Router

from src.filter.filter_ import IsPrivateChatTgBotFilter
from src.router import start, support, about, uploaded_pdf_file, uploaded_photo, convert_to_document

public_router = Router()

for observer in public_router.observers.values():
    observer.filter(IsPrivateChatTgBotFilter())

public_router.include_router(start.router)
public_router.include_router(support.router)
public_router.include_router(about.router)

public_router.include_router(uploaded_pdf_file.router)
public_router.include_router(uploaded_photo.router)
public_router.include_router(convert_to_document.router)


