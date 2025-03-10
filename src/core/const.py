import os
import pathlib

from arpakitlib.ar_enumeration_util import Enumeration

BASE_DIRPATH: str = str(pathlib.Path(__file__).parent.parent.parent)
SRC_DIRPATH: str = os.path.join(BASE_DIRPATH, "src")
RESOURCE_DIRPATH: str = os.path.join(BASE_DIRPATH, "resource")
ENV_FILENAME: str = ".env"
ENV_FILEPATH: str = os.path.join(BASE_DIRPATH, ENV_FILENAME)

PROMPT_TO_EXTRACT_TEXT_FROM_PHOTO = (
    "Проанализируй предоставленное изображение от пользователя и извлеки из него весь текст."
    "\nВыведи результат в виде строки (str), сохраняя регистр,"
    " знаки препинания и пробелы так, как они представлены на изображении."
    "\n\nВыводи только текст, который есть на картинке! Не нужно добовлять комментариев от себя."
)

class FileTypes(Enumeration):
    png = "png"
    jpg = "jpg"

class TypesOfFilesForConverting(Enumeration):
    docx = "docx"
    txt = "txt"
    md = "md"

class PublicTgBotCommands(Enumeration):
    start = "start"
    about = "about"
    support = "support"


# class PrivateTgBotCommands(Enumeration):
#     check_openai_api = "check_openai_api"
#     check_db = "check_db"
#     healthcheck = "healthcheck"
#     echo = "echo"
#     set_tg_bot_commands = "set_tg_bot_commands"
#     log_file = "log_file"
#     clear_log_file = "clear_log_file"
#     count_users = "count_users"
#     count_users_for_last_12_hours = "count_users_for_last_12_hours"
#     count_users_for_last_24_hours = "count_users_for_last_24_hours"
#     count_users_for_last_7_days = "count_users_for_last_7_days"


def __example():
    print("BASE_DIRPATH", BASE_DIRPATH)
    print("SRC_DIRPATH", SRC_DIRPATH)
    print("RESOURCE_DIRPATH", RESOURCE_DIRPATH)
    print("ENV_FILENAME", ENV_FILENAME)
    print("ENV_FILEPATH", ENV_FILEPATH)


if __name__ == '__main__':
    __example()
