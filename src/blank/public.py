from emoji import emojize

from src.core.const import PublicTgBotCommands, TypesOfFilesForConverting


class PublicTgBotBlank:

    @classmethod
    def command_to_desc(cls) -> dict[str, str]:
        return {
            PublicTgBotCommands.support: emojize(":red_heart: Поддержка"),
            PublicTgBotCommands.about: emojize(":information: Подробнее"),
            PublicTgBotCommands.start: emojize(":rocket: Начать")
        }

    @classmethod
    def error(cls) -> str:
        res = ":warning: <b>Произошла неполадка</b> :warning:"
        res += "\n\n:wrench: Мы уже исправляем её"
        res += (
            f"\n\n— Для оперативного решения вопросы обратитесь"
            f" в <a href='https://t.me/nurtdinov_gt'>поддержку</a>"
        )
        return emojize(res.strip())

    @classmethod
    def but_support(cls) -> str:
        return emojize(":red_heart: Поддержка")

    @classmethod
    def start(cls) -> str:
        return emojize(":waving_hand: Привет, просто отправь мне PDF документ или изображение, и я извлеку из него текст.")

    @classmethod
    def support(cls) -> str:
        res = f"🦦 По всем вопросам обращайтесь в <a href='https://t.me/nurtdinov_gt'>поддержку</a>"
        res += f"\n\n:link: https://t.me/nurtdinov_gt"
        return emojize(res.strip())

    @classmethod
    def about(cls) -> str:
        res = f":alien_monster: <b>Информация о боте:</b>\n"
        res += f"\nЭтот бот помогает извлекать текст из документов и изображений."
        res += f"\n\n<b>Возможности бота:</b>"
        res += f"\n- Распознавание текста из PDF и изображений (JPG, PNG)"
        res += f"\n- Конвертация текста в документы формата: DOCX, TXT, MD"
        res += f"\n\n<b>Как использовать?</b>"
        res += f"\n1. Отправьте PDF-документ или изображение с текстом."
        res += f"\n2. Бот обработает файл и покажет вам текст."
        res += f"\n3. Используйте кнопки для скачивания в удобном формате."
        res += (f"\n\n:link: <b>Поддержка:</b> https://t.me/nurtdinov_gt"
                f"\n:octopus: <b>Код проекта:</b> https://github.com/Gazinur16/ocr_text_from_docs_bot.git")
        return emojize(res.strip())

    @classmethod
    def image_is_loaded(cls) -> str:
        res = f":paperclip: <b>Изображение загружено!</b>"
        res += f"\n\n:magnifying_glass_tilted_left: Начинаю обработку, подождите..."
        return emojize(res.strip())

    @classmethod
    def difficult_case_please_wait(cls) -> str:
        res = f":sad_but_relieved_face: <b>Непростой случай.</b>"
        res += f"\n\n:hourglass_done: Пожалуйста, подождите еще немного..."
        return emojize(res.strip())

    @classmethod
    def doc_is_loaded(cls) -> str:
        res = f":paperclip: <b>Документ загружен!</b>"
        res += f"\n\n:magnifying_glass_tilted_left: Начинаю обработку, подождите немного..."
        return emojize(res.strip())

    @classmethod
    def failed_to_load_the_image(cls) -> str:
        res = f":warning: Не удалось загрузить изображение. Пожалуйста, попробуйте еще раз."
        return emojize(res.strip())

    @classmethod
    def convert_the_last_file(cls) -> str:
        res = f":sad_but_relieved_face: Конвертировать можно только последний загруженный вами файл."
        res += f"\n\n:information: Пожалуйста, загрузите фото или документ с текстом снова."
        return emojize(res.strip())

    @classmethod
    def not_found_the_full_text(cls) -> str:
        res = f":sad_but_relieved_face:  Не удалось найти текст."
        res += f"\n\n:information: Пожалуйста, загрузите фото или документ с текстом снова."
        return emojize(res.strip())

    @classmethod
    def text_is_successfully_converted(cls, file_type: str) -> str:
        res=f":check_mark_button: Текст успешно конвертирован в формат {file_type.upper()}"
        return emojize(res.strip())

    @classmethod
    def failed_to_find_the_text_in_the_photo(cls) -> str:
        res = f":sad_but_relieved_face: Упсс, не удалось найти текст на фото"
        res += f"\n\n:information:Пожалуйста, убедитесь что текст на фото видно хорошо, и попробуйте снова."
        return emojize(res.strip())

    @classmethod
    def failed_to_find_the_text_in_pdf(cls) -> str:
        res = f":sad_but_relieved_face: Упсс, не удалось найти текст в документе"
        res += f"\n\n:information:Пожалуйста, убедитесь что в документе есть текст, и попробуйте снова."
        return emojize(res.strip())

    @classmethod
    def the_text_was_cut(cls) -> str:
        res = f"\n:warning: <b>Текст был обрезан из-за ограничения Telegram </b>"
        res += f"\n\n:down_arrow: Для получения полного текста, можно скачать файл в одном из предложеных ниже вариантов."
        return emojize(res.strip())

    @classmethod
    def convert_and_download_file(cls) -> str:
        res = f":down_arrow: <b>Конвертировать и скачать файл в нужном формате.</b>"
        return emojize(res.strip())

    @classmethod
    def convert_to(cls, type_file: TypesOfFilesForConverting) -> str:
        if type_file is TypesOfFilesForConverting.docx:
            res = f":page_facing_up: Конвертировать в {TypesOfFilesForConverting.docx.upper()} (word)"
        elif type_file is TypesOfFilesForConverting.txt:
            res = f":spiral_notepad: Конвертировать в {TypesOfFilesForConverting.txt.upper()} (блокнот)"
        else:
            res = f":memo: Конвертировать в {TypesOfFilesForConverting.md.upper()} (markdown)"

        return emojize(res.strip())


def __example():
    pass


if __name__ == '__main__':
    __example()
