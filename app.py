import flask
import flask_cors
import pathlib


app: flask.Flask = flask.Flask(__name__)

flask_cors.CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        return flask.render_template("word_count_index.html")
    
    elif flask.request.method == "POST":
        file = flask.request.files.get("file")
        lines:int
        words: int
        bytes: int
        chars: int
        lines, words, bytes, chars = word_count(file)
        if flask.request.headers.get("Origin") == "http://localhost:5000":
            return flask.render_template("word_count.html", lines=lines ,words=words, bytes=bytes, chars=chars)
        else:
            return flask.jsonify({"lines":lines, "words":words, "bytes":bytes, "chars":chars})
    

def word_count(file)-> tuple[int, int, int, int]:
    """
    >>> file = pathlib.Path(__file__).absolute().parent / "test"  / "test.txt"
    >>> word_count(open(file, "rb"))
    (1364, 6288, 41577, 41335)
    """
    lines: int = -1
    words: int = 0
    bytes: int = -1
    chars: int = -1
    line: str
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