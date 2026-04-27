from enum import Enum
from dataclasses import dataclass
from typing import List


class TokenType(Enum):
    WORD = 'WORD'
    PIPE = 'PIPE'
    REDIR_IN = 'REDIR_IN'
    REDIR_OUT = 'REDIR_OUT'
    REDIR_APPEND = 'REDIR_APPEND'
    REDIR_ERR = 'REDIR_ERR'
    BG = 'BG'
    SEMI = 'SEMI'


@dataclass
class Token:
    type: TokenType
    value: str


def lex(line: str) -> List[Token]:
    """Tokenize a shell command line."""
    return []
