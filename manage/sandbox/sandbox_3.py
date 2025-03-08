import asyncio


def command():
    pass


async def __async_command():
    pass


if __name__ == '__main__':
    command()
    asyncio.run(__async_command())
