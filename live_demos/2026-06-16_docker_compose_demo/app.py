from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from a Dockerized Python webserver! 🐳\n"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # 0.0.0.0 so the server is reachable from outside the container
    app.run(host="0.0.0.0", port=8000)
