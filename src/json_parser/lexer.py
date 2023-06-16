import itertools
from typing import Optional

import more_itertools

from . import types
from . import subr


class Lexer:
    def __init__(self, chars):
        self.chars = more_itertools.peekable(chars)

    def consume(self) -> None:
        next(self.chars)

    def parse_string(self) -> types.TokenString:
        self.consume()  # consume start "
        s = ''.join(itertools.takewhile(lambda c: c != '"', self.chars))

        return types.TokenString(value=s)

    def parse_number(self) -> types.TokenInteger | types.TokenFloat:
        def pred(c: str) -> bool:
            return c in ('-', '+', '.', 'e', 'E') or c.isdigit()

        s = ''.join(subr.takewhile_inclusive(pred, self.chars))

        i, _ = subr.trap(lambda: int(s))
        if i is not None:
            return types.TokenInteger(value=i)

        f, _ = subr.trap(lambda: float(s))
        if f is not None:
            return types.TokenFloat(value=f)

        raise types.LexerError(f'Cannot parse as int/float: {s}')

    def next_token(self) -> Optional[types.Token]:
        peek: Optional[str] = self.chars.peek(None)

        if not peek:
            return None

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

        if peek in ('-', '+', '.') or peek.isdigit():
            return self.parse_number()

        if peek == '"':
            return self.parse_string()

        raise types.LexerError(f'Unexpected char: {peek}')

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
