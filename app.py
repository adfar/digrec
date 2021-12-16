from flask import Flask, render_template, request
from process import pinger, resize, to_json, predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["imgData"]
        pinger(data)
        digit = resize("img.png")
        prediction = predict(digit)
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')