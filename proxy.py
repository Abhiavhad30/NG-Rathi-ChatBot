from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/webhooks/rest/webhook", methods=["POST"])
def forward():
    try:
        response = requests.post("http://localhost:10000/webhooks/rest/webhook", json=request.get_json())
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
