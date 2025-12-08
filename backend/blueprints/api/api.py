import flask #Blueprint, request, render_template, Response
import flask_cors # cross_origin
from werkzeug.datastructures import FileStorage
import typing # Any
import pathlib # PATH
from ...word_count.wc import Data, word_count, word_count_empty


__all__: list[str] = ["api_bp"]


api_bp: flask.Blueprint = flask.Blueprint("api_bp", __name__) 


@api_bp.route("/api", methods=["POST"])
@flask_cors.cross_origin(origins=["https://sharrrkkk.github.io/", "http://localhost:8080"], supports_credentials=False)
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
    
    data: Data = word_count_empty('API')
    result: dict[str, typing.Any] = data._asdict()
    return flask.jsonify(result)


def _test()-> None:
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    _test()