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


class TokenNumber(Token):
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
