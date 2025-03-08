from emoji import demojize


def command():
    print(demojize(input(":")))


if __name__ == '__main__':
    command()