"""
Word Count package initializer.

Exposes core components for text file processing:

- Data              -> NamedTuple with mode, filename, line, word, byte, and character counts.
- word_count        -> Function to count lines, words, bytes, and characters in a file.
- word_count_empty  -> Function to return zeroed Data for empty or missing files.

Dependencies:
- wc.py contains the actual implementations.
"""
from .wc import Data, word_count, word_count_empty


__all__: list[str] = ["Data", "word_count", "word_count_empty"]