from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy credentials (you can replace with a real database later)
USERNAME = "Surya"
PASSWORD = "08102006"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return f"Welcome, {username}! Login successful."
        else:
            return "Login failed! Incorrect credentials."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)