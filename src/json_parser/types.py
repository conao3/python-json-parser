import enum

import pydantic


## Errors

class JsonParserError(Exception):
    pass


class LexerError(JsonParserError):
    pass


class ParserError(JsonParserError):
    pass


class UnexpectedTokenError(ParserError):
    pass


class Token(pydantic.BaseModel):
    pass


## Tokens

class TokenString(Token):
    value: str


class TokenNumber(Token):
    value: float


class TokenBooleanEnum(enum.Enum):
    TRUE = enum.auto()
    FALSE = enum.auto()


class TokenConst(Token):
    value: TokenBooleanEnum


class TokenNull(Token):
    pass


class TokenLeftBrace(Token):
    pass


class TokenRightBrace(Token):
    pass


class TokenLeftBracket(Token):
    pass


class TokenRightBracket(Token):
    pass


class TokenComma(Token):
    pass


class TokenColon(Token):
    pass
