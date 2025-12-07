from werkzeug.datastructures import FileStorage
import pathlib # PATH
import typing # BytesString, NamedTuple


__all__: list[str] = ["Data", "word_count", "word_count_empty"]


class Data(typing.NamedTuple):
    """
    Aggregated file statistics.

    Represents the results of `word_count`, containing line, word, byte,
    and character counts extracted from a UTF-8 text file.

    Attributes:
        lines (int): Total number of lines.
        words (int): Total number of whitespace-delimited words.
        bytes (int): Total number of raw bytes in the file.
        chars (int): Total number of UTF-8 decoded characters.
    """
    mode: str
    filename: str
    lines: int
    words: int
    bytes: int
    chars: int


def word_count(file: FileStorage, filename: str, mode: str)-> Data:
    """
    Count lines, words, bytes, and characters in a UTF-8 text file.

    This function reads a binary file-like object, decodes its content as UTF-8,
    and computes four statistics: the total number of lines, total words,
    the number of raw bytes, and the number of characters.

    Args:
        file (FileStorage): A binary file-like object opened in "rb" mode.
        filename (str): 
        mode (str): 

    Returns:
    Data (typing.NamedTuple): A NamedTuple with:
        - mode (str)
        - filename (str)
        - lines (int)
        - words (int)
        - bytes (int)
        - chars (int)

    Examples:
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test"  / "test.txt"
        >>> with open(filename, "rb") as file:
        ...     word_count(file, 'test.txt', 'SSR')
        Data(mode='SSR', filename='test.txt', lines=1364, words=6288, bytes=41577, chars=41335)
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test" / "spencer.jpg"
        >>> with open(filename, "rb") as file:
        ...     word_count(file, 'spencer.jpg', 'SSR')
        Data(mode='SSR', filename='spencer.jpg', lines=242, words=0, bytes=63496, chars=0)
    """
    lines: int = -1
    words: int = 0
    bytes: int = 0
    chars: int = 0
    line: typing.ByteString
    control: bool = _check_file_encoding(file)
    for line in file:
        lines += 1
        if len(line) > 0:
            words += len(line.split())
        bytes += len(line)
        if control:
            chars += len(line.decode("utf-8"))

    if control == False:
        words = 0
        chars = 0

    return Data(mode, filename, lines, words, bytes, chars)


def word_count_empty(mode: str)-> Data:
    """
    """
    return Data(mode, 'No File', 0, 0, 0, 0)


def _check_file_encoding(file: FileStorage)-> bool:
    """
    Check whether the uploaded file contains valid UTF-8 encoded text.

    Reads the first 2048 bytes of the uploaded file and attempts to decode them
    as UTF-8. If decoding succeeds, the file is considered UTF-8 text; otherwise
    it is treated as binary. The file stream position is restored after reading.

    Args:
        file (werkzeug.datastructures.FileStorage): The uploaded file stream
            provided by Flask/Werkzeug.

    Returns:
        bool: True if the file contains valid UTF-8 text, otherwise False.
    
    Examples:
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test" / "test.txt"
        >>> with open(filename, "rb") as file:
        ...     _check_file_encoding(file)
        True
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test" / "spencer.jpg"
        >>> with open(filename, "rb") as file:
        ...     _check_file_encoding(file)
        False
    """
    try:
        file.read(2048).decode("utf-8")
        file.seek(0)
        return True
    except UnicodeDecodeError:
        file.seek(0)
        return False


def _test()-> None:
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    _test()