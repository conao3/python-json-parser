from typing import Optional

import more_itertools

from . import types


class Lexer:
    def __init__(self, chars):
        self.chars = more_itertools.peekable(chars)

    def consume(self) -> None:
        next(self.chars)

    def parse_token(self, peek: str) -> types.Token:
        if peek.isspace():
            self.consume()
            return types.TokenWhiteSpace()

        raise types.LexerError(f'Unexpected char: {peek}')

    def next_token(self) -> Optional[types.Token]:
        peek = self.chars.peek(None)

        if not peek:
            return None

        return self.parse_token(peek)

    def tokenize(self) -> list[types.Token]:
        res = []
        while (token := self.next_token()):
            res.append(token)

        return res
