from flask import Flask, redirect, url_for
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the home page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"hello {name}!"

@app.route("/admin")
def admin():
    # return redirect(url_for("/"))
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)