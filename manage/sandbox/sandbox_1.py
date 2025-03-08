import asyncio

from emoji import emojize


def command():
    print("Hello" * 500)


async def __async_command():
    pass


if __name__ == '__main__':
    command()
    asyncio.run(__async_command())
