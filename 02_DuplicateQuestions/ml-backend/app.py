
"""
Imports
    * For ML model preperation refer to the main.py file
"""
import os,  json, time
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from flask import Flask, jsonify, request, make_response
import tensorflow as tf
from flask_cors import CORS

import numpy as np

from nltk.tokenize import word_tokenize

with open('data/word_indices.json', 'r') as reader:
    word_indices = json.loads(reader.read())

word_indices_reversed = dict([
    (v, k) for (k, v) in word_indices.items()
])
max_words = 100

def seq_to_text(sequences):
  return " ".join(word_indices_reversed[i] for i in sequences )

def text_to_seq(sent):
  words = word_tokenize(sent.lower())
  sequences = []
  for word in words:
    try:
      sequences.append(word_indices[word])
    except:
      sequences.append(0)
  return sequences

def text_to_padded_sequences(sent):
  tokens = text_to_seq(sent)
  padded_tokens = tf.keras.preprocessing.sequence.pad_sequences([tokens], maxlen=max_words,
                                                                padding="post", truncating="post")
  return padded_tokens

# The function that makes predictions

def predict(model, qn1, qn2):
  classes = ["not duplicate", "duplicate"]
  qn1_tokens = text_to_padded_sequences(qn1)
  qn2_tokens = text_to_padded_sequences(qn2)
  probability = tf.squeeze(model.predict([qn1_tokens, qn2_tokens]), 0)[0]
  classLabel = np.round(probability).astype('int32')

  probability = probability if probability >= .5  else 1- probability
  return {
    "class": classes[classLabel],
    "classLabel": f'{classLabel}',
    "probability": f'{probability:.4f}'
  }


"""
model loading
"""
question_model = tf.keras.models.load_model("model/questions_model.h5")
"""
flask application
"""
app = Flask(__name__)
CORS(app)
app.config["ENV"] = "development"



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