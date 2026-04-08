from flask import Flask, render_template, request
from PIL import Image
from utils import predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    
    if request.method == "POST":
        file = request.files["file"]
        image = Image.open(file)
        prediction = predict(image)
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)