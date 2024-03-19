from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    return "Machine Learning Model is Working"