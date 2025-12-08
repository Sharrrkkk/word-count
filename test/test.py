import pytest


__all__: list[str] = []


def _test_doctest()-> None:
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
    pytest.main(["--doctest-modules", "ignore=.'.*'", "../", "-vv"])


if __name__ == "__main__":
    _test_doctest()
