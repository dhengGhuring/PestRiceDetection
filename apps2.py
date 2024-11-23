from flask import Flask, request
import utils as util

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    coba = util.clasification()
    return coba


@app.route("/predict", methods=['POST'])
def predict():
    gambar = request.files.get('file')
    if gambar:
        coba = util.predict(gambar)
        return coba
    else:
        return "error"

if __name__ == "__main__":
    app.run(port=3000, debug=True)