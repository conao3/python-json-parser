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
            return types.const.TokenWhiteSpace

        if peek == '{':
            self.consume()
            return types.const.TokenLeftBrace

        if peek == '}':
            self.consume()
            return types.const.TokenRightBrace

        if peek == '[':
            self.consume()
            return types.const.TokenLeftBracket

        if peek == ']':
            self.consume()
            return types.const.TokenRightBracket

        if peek == ',':
            self.consume()
            return types.const.TokenComma

        if peek == ':':
            self.consume()
            return types.const.TokenColon

        if peek == 'n':
            s = ''.join(more_itertools.take(4, self.chars))
            if s == 'null':
                return types.const.TokenNull

        if peek == 't':
            s = ''.join(more_itertools.take(4, self.chars))
            if s == 'true':
                return types.const.TokenTrue

        if peek == 'f':
            s = ''.join(more_itertools.take(5, self.chars))
            if s == 'false':
                return types.const.TokenFalse

        raise types.LexerError(f'Unexpected char: {peek}')

    def next_token(self) -> Optional[types.Token]:
        peek = self.chars.peek(None)

        if not peek:
            return None

        return self.parse_token(peek)

    def tokenize(self) -> list[types.Token]:
        res = []
        while (token := self.next_token()):
            if (
                token is types.const.TokenWhiteSpace or
                isinstance(token, types.TokenWhiteSpace)
            ):
                continue

            res.append(token)

        return res
