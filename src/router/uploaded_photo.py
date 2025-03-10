import base64
import logging

from aiogram import types, Router
from aiogram.exceptions import AiogramError
from aiogram.fsm.context import FSMContext
from arpakitlib.ar_str_util import remove_tags_and_html
from arpakitlib.ar_type_util import raise_for_type

from src.blank.public import PublicTgBotBlank
from src.business_service.get_text_from_photo_with_mistral import get_text_from_photo_with_mistral
from src.business_service.get_text_from_photo_with_gpt import get_text_from_photo_with_gpt
from src.core.const import FileTypes
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsPrivateChatTgBotFilter, IsImageFileFilter
from src.kb.inline import conversion_of_text_to_file
from src.util.remove_markdown import remove_markdown

router = Router()
_logger = logging.getLogger(__name__)

@router.message(IsPrivateChatTgBotFilter(), IsImageFileFilter())
async def _(
        m: types.Message,
        state: FSMContext,
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
        try:
            await m.answer(text=PublicTgBotBlank.failed_to_load_the_image())
        except AiogramError as e:
            _logger.error(e)
        return

    file_bytes = await transmitted_tg_bot_data.tg_bot.download_file(file_path=tg_file.file_path)
    file_content = file_bytes.read()

    try:
        loaded_msg = await m.answer(text=PublicTgBotBlank.image_is_loaded())
    except AiogramError as e:
        loaded_msg = None
        _logger.error(e)

    text_from_photo_mistral = await get_text_from_photo_with_mistral(file_bytes=file_content, file_type=file_type)
    raise_for_type(text_from_photo_mistral, str)
    final_text_from_photo = remove_tags_and_html(remove_markdown(text_from_photo_mistral))

    if not final_text_from_photo:
        try:
            if loaded_msg:
                await loaded_msg.edit_text(text=PublicTgBotBlank.difficult_case_please_wait())
            else:
                await m.answer(text=PublicTgBotBlank.difficult_case_please_wait())
        except AiogramError as e:
            _logger.error(e)

        text_from_photo_gpt = await get_text_from_photo_with_gpt(file_bytes=file_content)
        raise_for_type(text_from_photo_gpt, str)
        final_text_from_photo = remove_tags_and_html(remove_markdown(text_from_photo_gpt))

        if not final_text_from_photo:
            try:
                if loaded_msg:
                    await loaded_msg.edit_text(text=PublicTgBotBlank.failed_to_find_the_text_in_the_photo())
                else:
                    await m.answer(text=PublicTgBotBlank.failed_to_find_the_text_in_the_photo())
            except AiogramError as e:
                _logger.error(e)
            return

    await state.update_data({f"last_message_id_from_{m.from_user.id}": loaded_msg.message_id})
    await state.update_data({f"text_from_{m.from_user.id}": final_text_from_photo})

    if len(final_text_from_photo) > 4096:
        ready_text_from_photo = final_text_from_photo[:3900] + "\n\n" + PublicTgBotBlank.the_text_was_cut()
    else:
        ready_text_from_photo = final_text_from_photo + "\n\n" +PublicTgBotBlank.convert_and_download_file()

    try:
        if loaded_msg:
            await loaded_msg.edit_text(text=ready_text_from_photo,
                                       reply_markup=conversion_of_text_to_file(message_id=m.message_id))
        else:
            await m.answer(text=ready_text_from_photo,
                           reply_markup=conversion_of_text_to_file(message_id=m.message_id))
    except AiogramError as e:
        _logger.error(e)
