from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

# Enable CORS for all origins (allow any website)
CORS(app)

FILE_PATH = "data.txt"

@app.route("/write", methods=["POST"])
def write_text():
    text = None

    if request.is_json:
        text = request.json.get("text")
    else:
        text = request.form.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
