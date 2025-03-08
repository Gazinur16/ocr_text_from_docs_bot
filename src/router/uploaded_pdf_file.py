from aiogram import types, Router

from src.business_service.get_text_from_pdf_doc import get_text_from_pdf_doc
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsPrivateChatTgBotFilter, IsPdfDocumentFilter

router = Router()

@router.message(IsPrivateChatTgBotFilter(), IsPdfDocumentFilter())
async def process_pdf(
        m: types.Message,
        transmitted_tg_bot_data: TransmittedTgBotData,
        **kwargs
):
    tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.document.file_id)
    file_bytes = await transmitted_tg_bot_data.tg_bot.download_file(file_path=tg_file.file_path)

    await m.answer(text="📎 Документ загружен! "
                        "\nНачинаю обработку, подождите немного...")

    text_from_pdf = await get_text_from_pdf_doc(file_bytes=file_bytes.read())
    print(text_from_pdf)
