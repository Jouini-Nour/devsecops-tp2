from flask import Flask, jsonify, request
import subprocess
import re

app = Flask(__name__)

USERS = {1: {"id": 1, "name": "alice"}, 2: {"id": 2, "name": "bob"}}


@app.route("/")
def index():
    return jsonify(status="ok", service="devsecops-demo")


@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = USERS.get(user_id)
    if user is None:
        return jsonify(error="not found"), 404
    return jsonify(user)


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]{0,252}", host):
        return jsonify(error="invalid host"), 400
    out = subprocess.run(["ping", "-c", "1", host],
                         capture_output=True, text=True, timeout=5)
    return jsonify(output=out.stdout)

@app.route("/echo")
def echo():
    msg = request.args.get("msg", "")
    return jsonify(message=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)