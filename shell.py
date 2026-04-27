#!/usr/bin/env python3
import sys
try:
    import readline  # noqa: F401
except ImportError:
    pass
from lexer import lex
from parser import parse
from executor import execute


def main():
    while True:
        try:
            line = input('pyshell> ')
            if not line.strip():
                continue
            tokens = lex(line)
            commands = parse(tokens)
            execute(commands)
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
