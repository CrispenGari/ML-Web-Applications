from flask import Flask, render_template, make_response, jsonify, request
import pickle
with open('../clf/models/sentiment_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
app.config.from_object("config.Development")

text = 'i watched gomeda on movie theater at my city my friend took away me and i was really curious what would be it looked like well i must say this movie was not a horror may be we can say that is fantsastic experimentation ok here i go anyway but there was a lot of shooting acting dramatic theatrical and storytelling problems i can understand because of director is very young and gomeda is his first feature film ok directing of this film was not pretty bad i see unfortunately due to the restraints placed on the film by its extremely low budget the visuals are often as murky as the storyline and there is no powerful gothic scenes as a horror movie it really fails no scares at all and it is quite muddled and boring some people say gomeda is an art movie but i could not see a laughable terrible and breoken off art movie like that so how can we say it is an art movie just funny '

class Sentiments:
    POSITIVE = {'id': 1, "sentiment": "POSITIVE"}
    NEGATIVE = {'id': 0, "sentiment": "NEGATIVE"}

sentiments = [
    Sentiments.NEGATIVE,
    Sentiments.POSITIVE
]

@app.errorhandler(404)
def error_404(e):
    status = 404
    return render_template('error.html', status=status), 404

@app.route("/home")
def home():
    return render_template('index.html'), 200

@app.route("/predict", methods=["GET","POST"])
def make_prediction():
    cookies = request.cookies
    prediction = model.predict([cookies["query"]])[0]
    if request.method == "GET":
        return make_response(
        jsonify(sentiments[prediction]), 200
        )
    else:
        return make_response(jsonify(
            {"code": 405,
             "message": "Method Not Allowed."
             }
        ), 405)
    return "Done", 200

if __name__ == '__main__':
    app.run(debug=True)