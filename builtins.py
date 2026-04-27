BUILTINS = {'cd', 'exit', 'pwd', 'export', 'unset', 'jobs', 'fg', 'bg'}


def builtin_cd(args: list) -> int:
    """Change directory."""
    pass


def builtin_exit(args: list) -> int:
    """Exit the shell."""
    pass


def builtin_pwd(args: list) -> int:
    """Print working directory."""
    pass


def builtin_export(args: list) -> int:
    """Export environment variable."""
    pass


def builtin_unset(args: list) -> int:
    """Unset environment variable."""
    pass


def builtin_jobs(args: list) -> int:
    """List background jobs."""
    pass


def builtin_fg(args: list) -> int:
    """Bring job to foreground."""
    pass


def builtin_bg(args: list) -> int:
    """Continue stopped job in background."""
    pass
