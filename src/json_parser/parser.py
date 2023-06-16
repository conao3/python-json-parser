from typing import Optional
import more_itertools
from . import types


class Parser:
    def __init__(self, tokens):
        self.tokens = more_itertools.peekable(tokens)

    def parse(self) -> Optional[types.Value]:
        peek: Optional[types.Token] = self.tokens.peek(None)

        return None
