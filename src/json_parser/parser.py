import more_itertools
from . import types


class Parser:
    def __init__(self, tokens):
        self.tokens = more_itertools.peekable(tokens)

    def parse(self) -> types.Value:
        return types.ValueObject(value={})
