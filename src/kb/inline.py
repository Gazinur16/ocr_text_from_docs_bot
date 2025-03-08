from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.blank.public import PublicTgBotBlank


def support_ikb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(InlineKeyboardButton(
        text=PublicTgBotBlank.but_support(),
        url="https://t.me/nurtdinov_gt"
    ))

    return kb_builder.as_markup()
