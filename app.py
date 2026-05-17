from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    address = data.get("address", "").strip()
    email = data.get("email", "").strip()

    if not all([name, phone, address, email]):
        return jsonify({"success": False, "message": "All fields are required."}), 400

    # TODO: Add your CRM / email integration here (e.g. send to a Google Sheet,
    # email via SendGrid, or POST to a webhook like Zapier).
    print(f"New lead: {name} | {phone} | {address} | {email}")

    return jsonify({"success": True, "message": "Thanks! We'll be in touch within 24 hours."})

if __name__ == "__main__":
    app.run(debug=True)
