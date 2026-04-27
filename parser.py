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
    return []
