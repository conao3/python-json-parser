from . import lexer


def read(arg: str) -> str:
    lexer_ = lexer.Lexer(arg)
    return str(lexer_.tokenize())


def eval(arg: str) -> str:
    return arg


def print(arg: str) -> str:
    return arg


def rep(arg: str) -> str:
    return print(eval(read(arg)))
