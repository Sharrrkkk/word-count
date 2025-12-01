import flask
import pathlib


app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        return flask.render_template("word_count_index.html")
    
    elif flask.request.method == "POST":
        file = flask.request.files.get("file")
        lines, words, bytes, chars = word_count(file)
        return flask.render_template("word_count.html", lines=lines ,words=words, bytes=bytes, chars=chars)


def word_count(file):
    """
    >>> file = pathlib.Path(__file__).absolute().parent / "test"  / "test.txt"
    >>> word_count(open(file, "rb"))
    (1364, 6288, 41577, 41335)
    """
    lines: int = -1
    words: int = 0
    bytes: int = -1
    chars: int = -1
    for line in file.read().decode("utf-8").split("\n"):
        lines += 1
        if len(line) > 0:
            words += len(line.split())
        bytes += len(line.encode()) + 1
        chars += len(line) + 1
    return (lines, words, bytes, chars)

    
def test()-> None:
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    #test()
    app.run(debug=True)