"""
Main Flask application module.

This module initializes the Flask app, configures CORS, and defines
the application's public endpoints:

- GET /               → Render the home page.
- POST /              → Process an uploaded file and display statistics.
- POST /api           → Return file statistics as JSON.
- POST /embedded      → Render an embedded page with file statistics.

The module depends on:
- flask: Core web framework.
- flask_cors: CORS support.
- pathlib: Filesystem path utilities.
- typing: Type annotations (ByteString, NamedTuple).

All text-file processing is delegated to `word_count()`, which returns
a `Data` NamedTuple with line, word, byte, and character counts.
"""
import flask #request, render_template, Response
import flask_cors # CORS
import pathlib # PATH
import typing # BytesString, NamedTuple
from werkzeug.datastructures import FileStorage
import sys # stderr


app: flask.Flask = flask.Flask(__name__)
flask_cors.CORS(app)


@app.route("/", methods=["GET", "POST"])
def home()-> flask.Response:
    """
    Render home page and handle file upload for counting.

    Handles GET requests by rendering the 'word_count_home.html' template.
    Handles POST requests by reading an uploaded text file, computing
    lines, words, bytes, and characters using `word_count()`, and
    rendering the results. If no file is uploaded, the template is
    rendered without counts.

    Args:
    file (FileStorage | None):
        Binary file-like object from request.files.get("file").
        None if no file was uploaded.

    Returns:
        flask.Response:
            HTML page rendered with the count statistics:
            - mode (str): Rendering mode
            - filename (str): full file name
            - lines (int): Total number of lines.
            - words (int): Total number of words.
            - bytes (int): Total byte size of the file.
            - chars (int): Total number of UTF-8 characters.

    Examples:
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test"  / "test.txt"
        >>> with open(filename, "rb") as file:
        ...     word_count(file, 'test.txt', 'SSR')
        Data(mode='SSR', filename='test.txt', lines=1364, words=6288, bytes=41577, chars=41335)
    """
    if flask.request.method == "GET":
        return flask.Response(flask.render_template("word_count_home.html"))
    
    elif flask.request.method == "POST":
        file: FileStorage | None = flask.request.files.get("file")
        if file and file.filename and len(file.filename) >= 0:
            data: Data = word_count(file, file.filename, 'SSR')
            mode: str = data.mode
            filename: str = data.filename
            lines: int = data.lines
            words: int = data.words
            bytes: int = data.bytes
            chars: int = data.chars
            return flask.Response(flask.render_template("word_count_home.html",
            mode=mode, filename=filename, lines=lines ,words=words, bytes=bytes,
            chars=chars))
        else:
            return flask.Response(flask.render_template("word_count_home.html",
            mode="SSR", filename='No file', lines=0 ,words=0, bytes=0, chars=0))
    else:
        return flask.Response(flask.render_template("word_count_home.html",
        mode='SSR', filename='No file', lines=0 ,words=0, bytes=0, chars=0))
    

@app.route("/embedded", methods=["POST"])
def embedded()-> flask.Response:
    """
    Process an uploaded text file and return line, word, byte, and character counts.

    Reads a text file uploaded via the form, counts lines, words, bytes,
    and characters using `word_count()`, and renders the results in the
    'word_count_embedded.html' template. If no file is uploaded, zeros
    are used for all counts.

    Args:
    file (FileStorage | None):
        Binary file-like object from request.files.get("file").
        None if no file was uploaded.

    Returns:
    flask.Response:
        Rendered HTML page containing the count statistics:
            - mode (str): Rendering mode
            - filename (str): full file name
            - lines (int): Total number of lines.
            - words (int): Total number of words.
            - bytes (int): Total byte size of the file.
            - chars (int): Total number of UTF-8 characters.

    Examples:
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test"  / "test.txt"
        >>> with open(filename, "rb") as file:
        ...     word_count(file, 'test.txt', 'EMBEDDED')
        Data(mode='EMBEDDED', filename='test.txt', lines=1364, words=6288, bytes=41577, chars=41335)
    """
    if flask.request.method == "POST":
        file: FileStorage | None = flask.request.files.get("file")
        if file and file.filename and len(file.filename) >= 0:
            data: Data = word_count(file, file.filename, 'EMBEDDED')
            mode: str = data.mode
            filename: str = data.filename
            lines: int = data.lines
            words: int = data.words
            bytes: int = data.bytes
            chars: int = data.chars
            return flask.Response(flask.render_template("word_count_embedded.html",
            mode=mode, filename=filename, lines=lines ,words=words, bytes=bytes,
            chars=chars))
        else:
            return flask.Response(flask.render_template("word_count_embedded.html",
            mode='EMBEDDED', filename='No file', lines=0 ,words=0, bytes=0, chars=0))   
    else:
        return flask.Response(flask.render_template("word_count_embedded.html",
        mode='EMBEDDED', filename='No file', lines=0 ,words=0, bytes=0, chars=0))
    

@app.route("/api", methods=["POST"])
def api()-> flask.Response:
    """
    Process an uploaded text file and return line, word, byte, and character counts.

    Handles a POST request containing a file under the "file" form field.
    If no file is provided, returns default counts with zeros.

    Args:
    file (FileStorage | None):
        Binary file-like object from request.files.get("file").
        None if no file was uploaded.

    Returns:
    flask.Response:
        HTTP JSON response containing:
            - mode (str): Rendering mode
            - filename (str): full file name
            - lines: Total number of lines.
            - words: Total number of words.
            - bytes: Total byte size of the file.
            - chars: Total number of UTF-8 characters.

    Examples:
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test"  / "test.txt"
        >>> with open(filename, "rb") as file:
        ...     word_count(file, 'test.txt', 'API')
        Data(mode='API', filename='test.txt', lines=1364, words=6288, bytes=41577, chars=41335)
    """
    if flask.request.method == "POST":
        file: FileStorage | None = flask.request.files.get("file")
        if file and file.filename and len(file.filename) >= 0:
            data: Data = word_count(file, file.filename, 'API')
            return flask.jsonify(data._asdict())
        else:
            return flask.jsonify(Data('API', 'No file', 0,0,0,0)._asdict())
    else:
        return flask.jsonify(Data('API', 'No file', 0,0,0,0)._asdict())
    

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
    control: bool = check_file_encoding(file)
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


def check_file_encoding(file: FileStorage)-> bool:
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
        ...     check_file_encoding(file)
        True
        >>> filename: pathlib.Path = pathlib.Path(__file__).absolute().parent / "test" / "spencer.jpg"
        >>> with open(filename, "rb") as file:
        ...     check_file_encoding(file)
        False
    """
    try:
        file.read(2048).decode("utf-8")
        file.seek(0)
        return True
    except UnicodeDecodeError:
        file.seek(0)
        return False

    
def test()-> None:
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
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    """
    Entry point used to run the Flask development server.

    This block ensures that the application only starts the local
    development server when executed directly, and not when imported
    as a module in another file. Debug mode is enabled to allow
    automatic reloads and detailed error messages during development.
    """
    test()
    #app.run(debug=True)