from typing import Literal

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.blank.public import PublicTgBotBlank
from src.kb.callback import BaseCD


class ConversionOfTextToFileCD(BaseCD):
    message_id: int
    type_file: Literal["docx", "txt", "md"]


def conversion_of_text_to_file(*, message_id: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(InlineKeyboardButton(
        text="DOCS",
        callback_data=ConversionOfTextToFileCD(message_id=message_id, type_file="docx").pack()
    ))

    kb_builder.add(InlineKeyboardButton(
        text="TXT",
        callback_data=ConversionOfTextToFileCD(message_id=message_id, type_file="txt").pack()
    ))

    kb_builder.add(InlineKeyboardButton(
        text="MD",
        callback_data=ConversionOfTextToFileCD(message_id=message_id, type_file="md").pack()
    ))

    return kb_builder.as_markup()

def support_ikb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(InlineKeyboardButton(
        text=PublicTgBotBlank.but_support(),
        url="https://t.me/nurtdinov_gt"
    ))

    return kb_builder.as_markup()
