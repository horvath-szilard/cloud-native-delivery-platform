import os
import socket

from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return {
        "application": "uptime-api",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)