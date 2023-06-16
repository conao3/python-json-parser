from . import types


class Lexer:
    def __init__(self, chars):
        self.chars = chars

    def tokenize(self) -> list[types.Token]:
        return []
