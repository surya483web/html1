from flask import Flask, request, jsonify

app = Flask(__name__)

PASSWORD = "08102006"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if password != PASSWORD:
        return jsonify({"status": "failed", "message": "Incorrect password"})
    
    if username != "Surya":
        return jsonify({"status": "failed", "message": "Incorrect username"})

    return jsonify({"status": "success", "message": f"Welcome {username}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)