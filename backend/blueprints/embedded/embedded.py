import flask #Blueprint, request, render_template, Response
import flask_cors # cross_origin
from werkzeug.datastructures import FileStorage
import typing # Any
import pathlib # PATH
from ...word_count.wc import Data, word_count, word_count_empty


__all__: list[str] = ["embedded_bp"]


embedded_bp: flask.Blueprint = flask.Blueprint("embedded_bp", __name__, template_folder="templates") 

flask_cors.CORS(embedded_bp, resources={r"/*": {
    "origins": 
        ["https://sharrrkkk.github.io/word-count/", 
        "https://sharrrkkk.github.io/*",
        "http://localhost:8080"]
}})


@embedded_bp.route("/embedded", methods=["POST"])
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
            result: dict[str, typing.Any] = data._asdict()
            return flask.Response(flask.render_template("word_count_embedded.html", **result))

    data: Data = word_count_empty('EMBEDDED')
    result: dict[str, typing.Any] = data._asdict()
    return flask.Response(flask.render_template("word_count_embedded.html", **result))


def _test()-> None:
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    _test()