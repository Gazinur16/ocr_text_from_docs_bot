from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.blank.public import PublicTgBotBlank


# def menu_skb() -> ReplyKeyboardMarkup:
#     kb_builder = ReplyKeyboardBuilder()
#
#     kb_builder.row(KeyboardButton(
#         text=PublicTgBotBlank.but_see_profiles()
#     ))
#
#     kb_builder.row(KeyboardButton(
#         text=PublicTgBotBlank.but_my_profile()
#     ))
#
#     return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=False, is_persistent=True)
