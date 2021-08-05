from flask import Flask, redirect, url_for
from tensorflow import keras
import tensorflow as tf
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the home page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"hello {name}!"

@app.route("/run")
def init():
    global sess
    sess = tf.compat.v1.Session()
    tf.compat.v1.keras.backend.set_session(sess)
    global model
    model = keras.models.load_model('checkpoint.h5', compile=False)
    global graph
    graph = tf.compat.v1.get_default_graph()
    return "<h1>model is available</h1>"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)