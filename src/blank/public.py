from emoji import emojize

from src.core.const import PublicTgBotCommands


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
        return emojize(":waving_hand:  Привет, просто отправь мне PDF документ или изображение, и я извлеку из него текст.")

    @classmethod
    def support(cls) -> str:
        res = f":red_heart: <b>Поддержка</b> :red_heart:"
        res += f"\n\n:link: https://t.me/nurtdinov_gt"
        return emojize(res.strip())

    @classmethod
    def about(cls) -> str:
        #TODO
        res = f":red_heart: НЕ ЗАБУДЬ ПРО ЭТО :red_heart:"
        return emojize(res.strip())


def __example():
    pass


if __name__ == '__main__':
    __example()
