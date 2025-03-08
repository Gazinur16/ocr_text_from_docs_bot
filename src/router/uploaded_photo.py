from aiogram import types, Router

from src.business_service.get_text_from_photo import get_text_from_photo
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsPrivateChatTgBotFilter, IsImageFileFilter

router = Router()

@router.message(IsPrivateChatTgBotFilter(), IsImageFileFilter())
async def process_photo(
        m: types.Message,
        transmitted_tg_bot_data: TransmittedTgBotData,
        **kwargs
):
    if m.photo:
        tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.photo[-1].file_id)
        file_type = "jpg"  # Telegram отправляет фото в JPEG
    elif m.document and m.document.mime_type.startswith("image/"):
        tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.document.file_id)
        file_type = "png" if m.document.mime_type == "image/png" else "jpg"
    else:
        await m.answer("⚠ Не удалось загрузить изображение. Попробуйте еще раз.")
        return

    file_bytes = await transmitted_tg_bot_data.tg_bot.download_file(file_path=tg_file.file_path)

    await m.answer(text="📎 Изображение загружено!"
                        "\nНачинаю обработку, подождите немного...")

    text_from_photo = await get_text_from_photo(file_bytes=file_bytes.read(), file_type=file_type)
    print(text_from_photo)
