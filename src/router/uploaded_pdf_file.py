import logging

from aiogram import types, Router
from aiogram.exceptions import AiogramError
from aiogram.fsm.context import FSMContext
from arpakitlib.ar_str_util import remove_tags_and_html
from arpakitlib.ar_type_util import raise_for_type

from src.blank.public import PublicTgBotBlank
from src.util.remove_markdown import remove_markdown
from src.business_service.get_text_from_pdf_doc_with_gpt import get_text_from_pdf_doc_with_gpt
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsPrivateChatTgBotFilter, IsPdfDocumentFilter
from src.kb.inline import conversion_of_text_to_file

router = Router()
_logger = logging.getLogger(__name__)

@router.message(IsPrivateChatTgBotFilter(), IsPdfDocumentFilter())
async def _(
        m: types.Message,
        state: FSMContext,
        transmitted_tg_bot_data: TransmittedTgBotData,
        **kwargs
):
    tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.document.file_id)
    file_bytes = await transmitted_tg_bot_data.tg_bot.download_file(file_path=tg_file.file_path)

    try:
        loaded_msg = await m.answer(text=PublicTgBotBlank.doc_is_loaded())
    except AiogramError as e:
        loaded_msg = None
        _logger.error(e)

    text_from_pdf = await get_text_from_pdf_doc_with_gpt(file_bytes=file_bytes.read())
    raise_for_type(text_from_pdf, str)
    final_text_from_pdf = remove_tags_and_html(remove_markdown(text_from_pdf))

    if not final_text_from_pdf:
        try:
            if loaded_msg:
                await loaded_msg.edit_text(text=PublicTgBotBlank.failed_to_find_the_text_in_pdf())
            else:
                await m.answer(text=PublicTgBotBlank.failed_to_find_the_text_in_pdf())
        except AiogramError as e:
            _logger.error(e)
        return

    await state.update_data({f"last_message_id_from_{m.from_user.id}": loaded_msg.message_id})
    await state.update_data({f"text_from_{m.from_user.id}": text_from_pdf})

    if len(text_from_pdf) > 4096:
        ready_text_from_pdf = final_text_from_pdf[:3900] + "\n\n" +PublicTgBotBlank.the_text_was_cut()
    else:
        ready_text_from_pdf = final_text_from_pdf + "\n\n" + PublicTgBotBlank.convert_and_download_file()

    try:
        if loaded_msg:
            await loaded_msg.edit_text(text=ready_text_from_pdf,
                                       reply_markup=conversion_of_text_to_file(message_id=m.message_id))
        else:
            await m.answer(text=ready_text_from_pdf,
                           reply_markup=conversion_of_text_to_file(message_id=m.message_id))
    except AiogramError as e:
        _logger.error(e)