import os
import pathlib

from arpakitlib.ar_enumeration_util import Enumeration

BASE_DIRPATH: str = str(pathlib.Path(__file__).parent.parent.parent)
SRC_DIRPATH: str = os.path.join(BASE_DIRPATH, "src")
RESOURCE_DIRPATH: str = os.path.join(BASE_DIRPATH, "resource")
ENV_FILENAME: str = ".env"
ENV_FILEPATH: str = os.path.join(BASE_DIRPATH, ENV_FILENAME)


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
