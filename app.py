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
import flask #Flask
from backend import home_bp, api_bp, embedded_bp


app: flask.Flask = flask.Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(api_bp)
app.register_blueprint(embedded_bp)


if __name__ == "__main__":
    """
    Entry point used to run the Flask development server.

    This block ensures that the application only starts the local
    development server when executed directly, and not when imported
    as a module in another file. Debug mode is enabled to allow
    automatic reloads and detailed error messages during development.
    """
    app.run(host="localhost", port=5000, debug=True)