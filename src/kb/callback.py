from aiogram.filters.callback_data import CallbackData

_used_cd_prefixes = set()


def get_used_cd_prefixes() -> set[str]:
    return _used_cd_prefixes


def generate_callback_data_prefix(string: str) -> str:
    res = 0
    for s_ in string:
        res += ord(s_)
    res += len(string)
    res = str(res)
    return res


class BaseCD(CallbackData, prefix="BaseCD"):

    def __init_subclass__(cls, **kwargs):
        if not cls.__name__.endswith("CD"):
            raise ValueError("callback data class should ends with CD")

        if "prefix" not in kwargs:
            kwargs["prefix"] = str(generate_callback_data_prefix(cls.__name__.lower().removesuffix("cd")))
        prefix = kwargs["prefix"]

        if prefix in _used_cd_prefixes:
            raise ValueError(f"prefix({prefix}) already in _used_cd_prefixes({_used_cd_prefixes})")
        _used_cd_prefixes.add(prefix)

        super().__init_subclass__(**kwargs)


class WithFromCD(BaseCD, prefix="WithFromCD"):
    from_: str | None = None
