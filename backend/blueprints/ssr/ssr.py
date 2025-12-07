import flask #Blueprint, request, render_template, Response
from werkzeug.datastructures import FileStorage
import typing # Any
import pathlib # PATH
from ...word_count.wc import Data, word_count, word_count_empty


__all__: list[str] = ["home_bp"]


home_bp: flask.Blueprint = flask.Blueprint("home_bp", __name__, template_folder="templates") 


@home_bp.route("/home", methods=["GET", "POST"])
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
            data: Data = word_count(file, file.filename, 'API')
            result: dict[str, typing.Any] = data._asdict()
            return flask.Response(flask.render_template("word_count_home.html", **result))
 
    data: Data = word_count_empty('API')
    result: dict[str, typing.Any] = data._asdict()
    return flask.Response(flask.render_template("word_count_home.html", **result))


def _test()-> None:
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    _test()