import os

from flask import Flask

app = Flask(__name__)

# Read configuration from environment variables, with sensible defaults
# so the app still runs if they aren't set.
GREETING = os.environ.get("GREETING", "Hello")
APP_ENV = os.environ.get("APP_ENV", "development")
DATA_FILE = os.environ.get("DATA_FILE", "data.txt")


def read_data_file():
    """Read the contents of the data file, or a friendly note if it's missing."""
    try:
        with open(DATA_FILE) as f:
            return f.read()
    except FileNotFoundError:
        return f"(no data file found at {DATA_FILE})"


@app.route("/")
def home():
    data = read_data_file()
    return f"""
    <html>
      <body>
        <h1>{GREETING} from a Dockerized Python webserver! 🐳</h1>
        <p><strong>Environment:</strong> {APP_ENV}</p>
        <h2>Data file ({DATA_FILE})</h2>
        <pre>{data}</pre>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # 0.0.0.0 so the server is reachable from outside the container
    app.run(host="0.0.0.0", port=8000)
