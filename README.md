# python-json-parser

A lightweight JSON parser implemented from scratch in Python. This project provides a clean lexer/parser architecture for parsing JSON documents into structured Python objects.

## Features

- Hand-written lexer and recursive descent parser
- Full JSON specification support (objects, arrays, strings, numbers, booleans, null)
- Type-safe AST representation using Pydantic models
- Interactive REPL for testing and exploration
- Clean separation between tokenization and parsing phases

## Requirements

- Python 3.11 or higher
- Poetry (for dependency management)

## Installation

```bash
git clone https://github.com/conao3/python-json-parser.git
cd python-json-parser
poetry install
```

## Usage

### Command Line REPL

Start the interactive parser:

```bash
poetry run json-parser
```

Example session:

```
user> {"name": "Alice", "age": 30}
value={'name': ValueString(value='Alice'), 'age': ValueInteger(value=30)}
user> [1, 2, 3, true, null]
value=[ValueInteger(value=1), ValueInteger(value=2), ValueInteger(value=3), ValueTrue(), ValueNull()]
```

### As a Library

```python
from json_parser import rep

result = rep.read('{"key": "value"}')
print(result)
```

## Project Structure

```
src/json_parser/
    lexer.py    # Tokenizer - converts input string to tokens
    parser.py   # Parser - converts tokens to AST
    types.py    # Token and Value type definitions
    rep.py      # Read-Eval-Print functions
    __main__.py # CLI entry point
```

## How It Works

1. **Lexer**: The input string is tokenized into a stream of tokens (braces, brackets, strings, numbers, keywords)
2. **Parser**: Tokens are consumed by a recursive descent parser that builds a typed AST
3. **Output**: The AST uses Pydantic models for type safety and easy serialization

## License

Apache-2.0
