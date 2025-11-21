from flask import Flask, request, Response ,jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/webhooks/rest/webhook", methods=["POST"])
def forward():
    try:
        r = requests.post(
            "http://localhost:10000/webhooks/rest/webhook",
            json=request.get_json(),
            timeout=30,
        )
        # Pass through Rasa's response exactly (including 500 body)
        return Response(r.content, status=r.status_code, headers={"Content-Type": r.headers.get("Content-Type", "application/json")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
