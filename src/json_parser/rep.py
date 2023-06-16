from typing import Optional
from . import lexer
from . import parser
from . import types


def read(arg: str) -> Optional[types.Value]:
    lexer_ = lexer.Lexer(arg)
    parser_ = parser.Parser(lexer_.tokenize())
    return parser_.parse()


def eval(arg: Optional[types.Value]) -> Optional[types.Value]:
    return arg


def print(arg: Optional[types.Value]) -> Optional[str]:
    if arg:
        return str(arg)

    return None


def rep(arg: str) -> Optional[str]:
    return print(eval(read(arg)))
