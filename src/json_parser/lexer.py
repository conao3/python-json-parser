from typing import Optional

import more_itertools

from . import types


class Lexer:
    def __init__(self, chars):
        self.chars = more_itertools.peekable(chars)

    def consume(self) -> None:
        next(self.chars)

    def next_token(self) -> Optional[types.Token]:
        peek = self.chars.peek(None)

        if not peek:
            return None

        if peek.isspace():
            self.consume()
            return types.TokenWhiteSpace()

        raise types.LexerError(f'Unexpected char: {peek}')

    def tokenize(self) -> list[types.Token]:
        res = []
        while (token := self.next_token()):
            res.append(token)

        return res
