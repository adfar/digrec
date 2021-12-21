from flask import Flask, render_template, request
from process import pinger, resize, to_json, predict, get_mapping

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["imgData"]
        pinger(data)
        digit = resize("img.png")
        prediction = predict(digit)
        mapping = get_mapping()
        prediction = chr(mapping[prediction])
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')