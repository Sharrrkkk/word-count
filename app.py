"""
Main Flask application module.

Initializes the Flask app and registers blueprints for the application.
All blueprints support file uploads.

- home_bp     → GET / and POST /, handles SSR pages and returns file statistics.
- api_bp      → POST /api, returns file statistics as JSON.
- embedded_bp → POST /embedded, renders embedded pages with file stats.

Dependencies:
- flask: Core web framework.
- flask_cors: CORS support.
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