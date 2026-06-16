import os
from pathlib import Path

from flask import Flask

app = Flask(__name__)

GREETING = os.environ.get("GREETING", "Hello")
APP_ENV = os.environ.get("APP_ENV", "development")
INPUT_DIR = Path(os.environ.get("INPUT_DIR", "/mnt/input"))
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/mnt/output"))


def read_file(path):
    try:
        return path.read_text()
    except Exception as e:
        return f"(error: {e})"


def process(content):
    """Toy transformation: word count header + uppercased content."""
    words = len(content.split())
    lines = len(content.splitlines())
    return f"lines={lines} words={words}\n{'=' * 30}\n{content.upper()}"


@app.route("/")
def home():
    input_files = sorted(INPUT_DIR.glob("*.txt")) if INPUT_DIR.exists() else []
    output_files = sorted(OUTPUT_DIR.glob("processed_*.txt")) if OUTPUT_DIR.exists() else []

    input_html = "".join(
        f"<h3>{f.name}</h3><pre>{read_file(f)}</pre>" for f in input_files
    ) or f"<p>(no .txt files found in {INPUT_DIR})</p>"

    output_html = "".join(
        f"<h3>{f.name}</h3><pre>{read_file(f)}</pre>" for f in output_files
    ) or "<p>(no output yet — click Process)</p>"

    return f"""<html><body>
      <h1>{GREETING} 🐳</h1>
      <p><strong>Environment:</strong> {APP_ENV}</p>
      <form method="POST" action="/process">
        <button type="submit">Process input files</button>
      </form>
      <h2>Input — <code>{INPUT_DIR}</code> (read-only)</h2>
      {input_html}
      <h2>Output — <code>{OUTPUT_DIR}</code> (read-write)</h2>
      {output_html}
    </body></html>"""


@app.route("/process", methods=["POST"])
def run_process():
    input_files = sorted(INPUT_DIR.glob("*.txt")) if INPUT_DIR.exists() else []
    results = []
    for f in input_files:
        out = OUTPUT_DIR / f"processed_{f.name}"
        out.write_text(process(f.read_text()))
        results.append(f.name)

    summary = f"Processed: {', '.join(results)}" if results else "No input files found."
    return f"""<html><body>
      <p>{summary}</p>
      <a href="/">Back</a>
    </body></html>"""


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
