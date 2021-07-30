import os, time
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from flask import Flask, jsonify,request, make_response
import tensorflow as tf
from main import predict

app = Flask(__name__)
app.config["ENV"] = "development"

question_model = tf.keras.models.load_model("model/questions_model.h5")

# print(question_model.summary())

def predictLabel(question1, question2):
    start = time.time()
    results = predict(question_model, question1, question2)
    end = time.time()
    results["time"] = f"{end - start}s"
    return results

@app.route('/', methods=["GET", "POST"])
def home():
    return make_response(jsonify({
        "name": "flask backend",
        "programmer": "Gari",
        "behind": "tensorflow and keras",
        "language": "python 3x",
    })), 200

@app.route('/predict', methods=["POST"])
def call():
    if request.method != "POST":
        return make_response(jsonify(
            {
                "error": "Only POST method are allowed.",
                "code": 500,
                "message": "Internal Server Error."
            }
        )), 500
    else:
        if request.is_json:
            res = request.get_json()
            return make_response(jsonify(
                predictLabel(res.get("question1"), res.get("question2"))
            )), 200
        else:
            return make_response(jsonify({
                "error": "Only JSON allowed in the post.",
                "code": 500,
                "message": "Internal Server Error."
            })), 500
    pass

if __name__ == '__main__':
    app.run(debug=True)