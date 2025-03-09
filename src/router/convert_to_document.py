import logging
import uuid

from aiogram import Router, types
from aiogram.exceptions import AiogramError
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.blank.public import PublicTgBotBlank
from src.business_service.converters import convert_to_docx, convert_to_txt, convert_to_md
from src.core.const import TypesOfFilesForConverting
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsPrivateChatTgBotFilter
from src.kb.inline import ConversionOfTextToFileCD

router = Router()
_logger = logging.getLogger(__name__)


@router.callback_query(
    ConversionOfTextToFileCD.filter(),
    IsPrivateChatTgBotFilter(),
    StateFilter("*")
)
async def _(cq: types.CallbackQuery,
            transmitted_tg_bot_data: TransmittedTgBotData,
            state: FSMContext,
            callback_data: ConversionOfTextToFileCD,
            **kwargs):

    state_data = await state.get_data()
    full_text = state_data.get(f"text_from_{callback_data.message_id}")

    if not full_text:
        try:
            await cq.answer(text=PublicTgBotBlank.not_found_the_full_text(), show_alert=True)
            await cq.message.edit_reply_markup(reply_markup=None)
        except AiogramError:
            pass
        return

    if callback_data.type_file == TypesOfFilesForConverting.docx:
        file_buffer = convert_to_docx(full_text=full_text)
        file_type = TypesOfFilesForConverting.docx
    elif callback_data.type_file == TypesOfFilesForConverting.txt:
        file_buffer = convert_to_txt(full_text=full_text)
        file_type = TypesOfFilesForConverting.txt
    else:
        file_buffer = convert_to_md(full_text=full_text)
        file_type = TypesOfFilesForConverting.md


    file_name = f"{uuid.uuid4().hex[:12]}.{file_type}"
    try:
        await transmitted_tg_bot_data.tg_bot.send_document(
            chat_id=cq.from_user.id,
            document=types.BufferedInputFile(file_buffer.getvalue(), filename=file_name)
        )
        await cq.answer(text=PublicTgBotBlank.text_is_successfully_converted(file_type=file_type))
    except AiogramError as e:
        _logger.error(e)