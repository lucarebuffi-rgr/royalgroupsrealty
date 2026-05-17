import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Paste your Make.com webhook URL here ──
MAKE_WEBHOOK = https://hook.us2.make.com/xa7uddev8m89ceqd97d9iurxyquirtn7

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data    = request.get_json()
    name    = data.get("name", "").strip()
    phone   = data.get("phone", "").strip()
    address = data.get("address", "").strip()
    email   = data.get("email", "").strip()

    if not all([name, phone, address, email]):
        return jsonify({"success": False, "message": "All fields are required."}), 400

    try:
        requests.post(MAKE_WEBHOOK, json={
            "name":    name,
            "phone":   phone,
            "address": address,
            "email":   email
        })
    except Exception as e:
        print(f"Make.com error: {e}")

    return jsonify({"success": True, "message": "Thanks! We'll be in touch within 24 hours."})

if __name__ == "__main__":
    app.run(debug=True)
