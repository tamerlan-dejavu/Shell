from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Command:
    argv: List[str]
    infile: Optional[str] = None
    outfile: Optional[str] = None
    errfile: Optional[str] = None
    append: bool = False
    background: bool = False
    next_pipe: Optional['Command'] = field(default=None, repr=False)


def parse(tokens: list) -> List[Command]:
    """Parse tokens into a list of commands."""
    if not tokens:
        return []

    commands = []
    current_argv = []
    infile = None
    outfile = None
    errfile = None
    append = False
    background = False
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token.type.name == 'WORD':
            current_argv.append(token.value)

        elif token.type.name == 'REDIR_IN':
            i += 1
            if i < len(tokens):
                infile = tokens[i].value

        elif token.type.name == 'REDIR_OUT':
            i += 1
            append = False
            if i < len(tokens):
                outfile = tokens[i].value

        elif token.type.name == 'REDIR_APPEND':
            i += 1
            append = True
            if i < len(tokens):
                outfile = tokens[i].value

        elif token.type.name == 'REDIR_ERR':
            i += 1
            if i < len(tokens):
                errfile = tokens[i].value

        elif token.type.name == 'PIPE':
            if current_argv:
                cmd = Command(
                    argv=current_argv,
                    infile=infile,
                    outfile=outfile,
                    errfile=errfile,
                    append=append,
                    background=False
                )
                commands.append(cmd)
                current_argv = []
                infile = outfile = errfile = None
                append = False

        elif token.type.name == 'BG':
            background = True

        elif token.type.name == 'SEMI':
            if current_argv:
                cmd = Command(
                    argv=current_argv,
                    infile=infile,
                    outfile=outfile,
                    errfile=errfile,
                    append=append,
                    background=background
                )
                commands.append(cmd)
                current_argv = []
                infile = outfile = errfile = None
                append = False
                background = False

        i += 1

    # Add the last command
    if current_argv:
        cmd = Command(
            argv=current_argv,
            infile=infile,
            outfile=outfile,
            errfile=errfile,
            append=append,
            background=background
        )
        commands.append(cmd)

    return commands
