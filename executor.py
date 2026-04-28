import subprocess
import sys
from typing import List
from parser import Command


def execute(commands: List[Command]) -> None:
    """Execute a list of commands."""
    if not commands:
        return

    # Handle pipes between commands
    processes = []
    prev_process = None

    for i, cmd in enumerate(commands):
        stdin = subprocess.PIPE if prev_process else None
        stdout = subprocess.PIPE if i < len(commands) - 1 else None
        stderr = subprocess.PIPE if cmd.errfile else None

        # Handle input redirection
        if cmd.infile:
            try:
                stdin = open(cmd.infile, 'r')
            except FileNotFoundError:
                print(f"pyshell: {cmd.infile}: No such file or directory", file=sys.stderr)
                return

        # Handle output redirection
        if cmd.outfile:
            mode = 'a' if cmd.append else 'w'
            try:
                stdout = open(cmd.outfile, mode)
            except IOError as e:
                print(f"pyshell: {cmd.outfile}: {e}", file=sys.stderr)
                return

        # Handle error redirection
        if cmd.errfile:
            try:
                stderr = open(cmd.errfile, 'w')
            except IOError as e:
                print(f"pyshell: {cmd.errfile}: {e}", file=sys.stderr)
                return

        try:
            # Create the process
            process = subprocess.Popen(
                cmd.argv,
                stdin=prev_process.stdout if prev_process else stdin,
                stdout=stdout,
                stderr=stderr,
                text=True
            )
            processes.append(process)

            # Close the previous stdout if piping
            if prev_process and prev_process.stdout:
                prev_process.stdout.close()

            prev_process = process

        except FileNotFoundError:
            print(f"pyshell: {cmd.argv[0]}: command not found", file=sys.stderr)
            return
        except Exception as e:
            print(f"pyshell: {e}", file=sys.stderr)
            return

    # Wait for all processes to complete
    for process in processes:
        try:
            process.wait()
        except KeyboardInterrupt:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
