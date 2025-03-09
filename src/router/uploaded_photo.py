from aiogram import types, Router

from src.blank.public import PublicTgBotBlank
from src.business_service.get_text_from_photo import get_text_from_photo
from src.core.const import FileTypes
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsPrivateChatTgBotFilter, IsImageFileFilter

router = Router()

@router.message(IsPrivateChatTgBotFilter(), IsImageFileFilter())
async def _(
        m: types.Message,
        transmitted_tg_bot_data: TransmittedTgBotData,
        **kwargs
):
    if m.photo:
        tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.photo[-1].file_id)
        file_type = FileTypes.jpg
    elif m.document and m.document.mime_type.startswith("image/"):
        tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.document.file_id)
        file_type = FileTypes.png if m.document.mime_type == "image/png" else FileTypes.jpg
    else:
        await m.answer(text=PublicTgBotBlank.failed_to_load_the_image())
        return

    file_bytes = await transmitted_tg_bot_data.tg_bot.download_file(file_path=tg_file.file_path)

    loaded_msg = await m.answer(text=PublicTgBotBlank.image_is_loaded())

    text_from_photo = await get_text_from_photo(file_bytes=file_bytes.read(), file_type=file_type)

    if not text_from_photo:
        await loaded_msg.edit_text(text="Не удалось найти текст 🥹"
                                       "Пожалуйста, убедитесь что в документе есть текст, и попробуйте снова.")
        return

    await loaded_msg.edit_text(text=text_from_photo)
