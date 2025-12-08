import pytest
import os
import pathlib


__all__: list[str] = []


def _test_doctest():
    """
    Run all doctests in the current module.

    This function imports Python's built-in doctest module and executes
    all doctests found in the file. It is mainly used during development
    to verify that example-based tests behave as expected.

    Args:
        None

    Returns:
        None
    """
    test_path: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
    os.chdir(test_path)
    return pytest.main(["--doctest-modules", ".", "-vv"])


if __name__ == "__main__":
    raise SystemExit(_test_doctest())