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
    tokens = []
    i = 0
    while i < len(line):
        # Skip whitespace
        if line[i].isspace():
            i += 1
            continue

        # Handle pipes
        if line[i] == '|':
            tokens.append(Token(TokenType.PIPE, '|'))
            i += 1
            continue

        # Handle redirections
        if line[i:i+2] == '>>':
            tokens.append(Token(TokenType.REDIR_APPEND, '>>'))
            i += 2
            continue
        if line[i:i+2] == '2>':
            tokens.append(Token(TokenType.REDIR_ERR, '2>'))
            i += 2
            continue
        if line[i] == '>':
            tokens.append(Token(TokenType.REDIR_OUT, '>'))
            i += 1
            continue
        if line[i] == '<':
            tokens.append(Token(TokenType.REDIR_IN, '<'))
            i += 1
            continue

        # Handle background
        if line[i] == '&':
            tokens.append(Token(TokenType.BG, '&'))
            i += 1
            continue

        # Handle semicolon
        if line[i] == ';':
            tokens.append(Token(TokenType.SEMI, ';'))
            i += 1
            continue

        # Handle quoted strings
        if line[i] in ('"', "'"):
            quote = line[i]
            j = i + 1
            while j < len(line) and line[j] != quote:
                j += 1
            tokens.append(Token(TokenType.WORD, line[i+1:j]))
            i = j + 1
            continue

        # Handle regular words
        j = i
        while j < len(line) and not line[j].isspace() and line[j] not in '|<>&;':
            j += 1
        if i < j:
            tokens.append(Token(TokenType.WORD, line[i:j]))
        i = j

    return tokens
