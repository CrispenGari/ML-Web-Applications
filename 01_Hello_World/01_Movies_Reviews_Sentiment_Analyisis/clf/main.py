import pickle
import numpy as np

with open('models/sentiment_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

text = 'i watched gomeda on movie theater at my city my friend took away me and i was really curious what would be it looked like well i must say this movie was not a horror may be we can say that is fantsastic experimentation ok here i go anyway but there was a lot of shooting acting dramatic theatrical and storytelling problems i can understand because of director is very young and gomeda is his first feature film ok directing of this film was not pretty bad i see unfortunately due to the restraints placed on the film by its extremely low budget the visuals are often as murky as the storyline and there is no powerful gothic scenes as a horror movie it really fails no scares at all and it is quite muddled and boring some people say gomeda is an art movie but i could not see a laughable terrible and breoken off art movie like that so how can we say it is an art movie just funny '
print(np.squeeze([model.predict([text])], axis=1))