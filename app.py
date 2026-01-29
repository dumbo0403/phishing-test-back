from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

FILE_PATH = "data.txt"

@app.route("/write", methods=["POST"])
def write_text():
    data = request.get_json(silent=True)
    text = data.get("text") if data else None

    if not text:
        return jsonify({"error": "No text provided"}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")

    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text} | IP={ip} | UA={ua}\n")

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
