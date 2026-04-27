import subprocess
import sys


def test_shell_import():
    """Test that shell module can be imported without errors."""
    result = subprocess.run(
        [sys.executable, '-c', 'import shell'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Shell import failed: {result.stderr}"


def test_shell_help():
    """Test that shell can be called with help flag."""
    result = subprocess.run(
        [sys.executable, 'shell.py', '--help'],
        capture_output=True,
        text=True,
        timeout=2
    )
    assert result.returncode in (0, 1), "Shell exited with unexpected code"
