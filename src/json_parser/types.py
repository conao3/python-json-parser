import enum

import pydantic


## Errors

class JsonParserError(Exception):
    pass


class LexerError(JsonParserError):
    pass


class ParserError(JsonParserError):
    pass


## Tokens

class Token(pydantic.BaseModel):
    pass


class TokenString(Token):
    value: str


class TokenInteger(Token):
    value: int


class TokenFloat(Token):
    value: float


class TokenTrue(Token):
    pass


class TokenFalse(Token):
    pass


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


class TokenWhiteSpace(Token):
    pass


class Const(pydantic.BaseModel):
    TokenTrue: TokenTrue
    TokenFalse: TokenFalse
    TokenNull: TokenNull
    TokenLeftBrace: TokenLeftBrace
    TokenRightBrace: TokenRightBrace
    TokenLeftBracket: TokenLeftBracket
    TokenRightBracket: TokenRightBracket
    TokenComma: TokenComma
    TokenColon: TokenColon
    TokenWhiteSpace: TokenWhiteSpace


const = Const(
    TokenTrue=TokenTrue(),
    TokenFalse=TokenFalse(),
    TokenNull=TokenNull(),
    TokenLeftBrace=TokenLeftBrace(),
    TokenRightBrace=TokenRightBrace(),
    TokenLeftBracket=TokenLeftBracket(),
    TokenRightBracket=TokenRightBracket(),
    TokenComma=TokenComma(),
    TokenColon=TokenColon(),
    TokenWhiteSpace=TokenWhiteSpace(),
)


# Values

class Value(pydantic.BaseModel):
    pass


class ValueObject(Value):
    value: dict[str, Value]


class ValueArray(Value):
    value: list[Value]


class ValueString(Value):
    value: str


class ValueInteger(Value):
    value: int


class ValueFloat(Value):
    value: float


class ValueTrue(Value):
    pass


class ValueFalse(Value):
    pass


class ValueNull(Value):
    pass
