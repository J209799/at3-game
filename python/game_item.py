from collections.abc import Callable  # noqa: INP001

from backpack import BackPack


class GameItem:
    def __init__(self, is_static: bool, conditional: Callable[[BackPack, str], bool]) -> None:
        self.is_static = is_static
        self.conditional = conditional
