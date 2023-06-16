from typing import Optional
import typing
import more_itertools
from . import types


class Parser:
    def __init__(self, tokens):
        self.tokens = more_itertools.peekable(tokens)

    def consume(self) -> types.Token:
        return next(self.tokens)

    T = typing.TypeVar('T', bound=types.Token)
    def expect(self, token: type[T]) -> T:
        t = self.consume()
        if not isinstance(t, token):
            raise types.ParserError(f'Expected {token}, got {t}')

        return t

    def parse_object(self) -> types.Value:
        self.consume()  # consume start {
        d: dict[str, types.Value] = {}

        if self.tokens.peek(None) is types.const.TokenRightBrace:
            return types.ValueObject(value=d)

        while True:
            key = self.expect(types.TokenString)
            _ = self.expect(types.TokenColon)
            val = self.parse()

            if not val:
                raise types.ParserError(f'Expected value, got no value')

            d[key.value] = val

            if self.tokens.peek(None) is types.const.TokenRightBrace:
                break

            _ = self.expect(types.TokenComma)

        self.consume()  # consume end }

        return types.ValueObject(value=d)

    def parse_array(self) -> types.Value:
        self.consume()  # consume start [
        l: list[types.Value] = []

        if self.tokens.peek(None) is types.const.TokenRightBracket:
            return types.ValueArray(value=l)

        while True:
            val = self.parse()

            if not val:
                raise types.ParserError(f'Expected value, got no value')

            l.append(val)

            if self.tokens.peek(None) is types.const.TokenRightBracket:
                break

            _ = self.expect(types.TokenComma)

        self.consume()  # consume end ]

        return types.ValueArray(value=l)

    def parse(self) -> Optional[types.Value]:
        peek: Optional[types.Token] = self.tokens.peek(None)

        if peek is types.const.TokenTrue:
            self.consume()
            return types.const.ValueTrue

        if peek is types.const.TokenFalse:
            self.consume()
            return types.const.ValueFalse

        if peek is types.const.TokenNull:
            self.consume()
            return types.const.ValueNull

        if isinstance(peek, types.TokenString):
            self.consume()
            return types.ValueString(value=peek.value)

        if isinstance(peek, types.TokenInteger):
            self.consume()
            return types.ValueInteger(value=peek.value)

        if isinstance(peek, types.TokenFloat):
            self.consume()
            return types.ValueFloat(value=peek.value)

        if peek is types.const.TokenLeftBrace:
            return self.parse_object()

        if peek is types.const.TokenRightBrace:
            raise types.ParserError(f'Unexpected token: {peek}')

        if peek is types.const.TokenLeftBracket:
            return self.parse_array()

        if peek is types.const.TokenRightBracket:
            raise types.ParserError(f'Unexpected token: {peek}')

        return None
