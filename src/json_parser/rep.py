from . import lexer
from . import parser
from . import types


def read(arg: str) -> types.Value:
    lexer_ = lexer.Lexer(arg)
    parser_ = parser.Parser(lexer_.tokenize())
    return parser_.parse()


def eval(arg: types.Value) -> types.Value:
    return arg


def print(arg: types.Value) -> str:
    return str(arg)


def rep(arg: str) -> str:
    return print(eval(read(arg)))
