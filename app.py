from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "message": "Hello from Flask Docker container v2",
        "app": "ecr-lab",
        "environment": os.environ.get("APP_ENV", "local")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "app": "ecr-lab",
        "environment": os.environ.get("APP_ENV", "local")
    })


@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello {name}",
        "app": "ecr-lab",
        "environment": os.environ.get("APP_ENV", "local")
    })

@app.route("/secret-status")
def secret_status():
    secret = os.environ.get("APP_SECRET")
    return jsonify({
        "secret_loaded": secret is not None and len(secret) > 0
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)