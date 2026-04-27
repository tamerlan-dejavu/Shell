# PYSHELL

A Unix-like shell implementation in Python for exploring computer architecture and operating systems concepts.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

To start the shell:

```bash
python shell.py
```

Then enter your shell commands at the `pyshell> ` prompt.

## Project Structure

- `shell.py` - Main REPL loop
- `lexer.py` - Tokenization of shell commands
- `parser.py` - Parsing tokens into command structures
- `executor.py` - Command execution engine
- `builtins.py` - Built-in shell commands (cd, exit, pwd, etc.)
- `jobs.py` - Job management and background processes
- `signals_handler.py` - Signal handling for process control
- `tests/` - Test suite
- `docs/` - Documentation

## Development

Run tests:
```bash
make test
```

Check code style:
```bash
make lint
```

Clean build artifacts:
```bash
make clean
```

## Features

- Command parsing and execution
- Pipe support
- Input/output redirection
- Background job management
- Built-in commands
