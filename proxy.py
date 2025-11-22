from flask import Flask, request, Response, jsonify
import requests
import time

app = Flask(__name__)

def wait_for_rasa():
    for _ in range(30):  # wait up to 60 seconds
        try:
            r = requests.get("http://127.0.0.1:10000/version", timeout=5)
            if r.status_code == 200:
                print("✅ Rasa is ready")
                return True
        except Exception as e:
            print(f"⏳ Waiting for Rasa: {e}")
        time.sleep(2)
    return False

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/webhooks/rest/webhook", methods=["POST"])
def forward():
    print("📨 Incoming request to /webhooks/rest/webhook")
    if not wait_for_rasa():
        print("❌ Rasa not ready")
        return jsonify({"error": "Rasa not ready"}), 503
    try:
        r = requests.post(
            "http://127.0.0.1:10000/webhooks/rest/webhook",
            json=request.get_json(force=True),
            timeout=30,
        )
        print(f"✅ Rasa responded with status {r.status_code}")
        print(f"➡️ Response body: {r.text}")
        return Response(
            r.content,
            status=r.status_code,
            headers={"Content-Type": r.headers.get("Content-Type", "application/json")},
        )
    except Exception as e:
        print(f"❌ Proxy error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run Flask on port 5000 so Render detects it
    app.run(host="0.0.0.0", port=5000)
