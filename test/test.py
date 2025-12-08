"""
Test runner module.

Provides a helper function to run all doctests in the project using pytest,
adjusting the working directory to the project root before execution.

Modules:
    pytest: Runs doctests and collects results.
    os: Changes the working directory.
    pathlib: Resolves paths.

__all__:
    Empty, as this module is intended for internal test execution.
"""
import pytest # main
import os # chdir
import pathlib # Path


__all__: list[str] = []


def _test_doctest():
    """
    Run all doctests in the project.

    Changes the working directory to the project root and executes pytest
    with doctest enabled, ensuring all modules are tested consistently.

    Args:
        None

    Returns:
        int: Exit code returned by pytest.
    """
    test_path: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
    os.chdir(test_path)
    return pytest.main(["--doctest-modules", ".", "-vv"])


if __name__ == "__main__":
    """
    Entry point used when running this module directly.

    When the file is executed as a script (e.g., `python3 test.py`), this block
    invokes `_test_doctest()` and immediately terminates the process with itsecho
    result code by raising `SystemExit`.

    Using `raise SystemExit(...)` ensures that any exit status returned by
    pytest/doctest is propagated to the calling shell, allowing proper failure
    detection in CI/CD pipelines or external scripts.
    """
    raise SystemExit(_test_doctest())