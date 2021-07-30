
"""
THIS CODE IS TAKEN FROM:
  https://github.com/CrispenGari/nlp-tensorflow/blob/main/06_Duplicate_Questions/01_Questions_Pairs_RNN.ipynb
"""
import os, sys, json, time
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
import pandas as pd
import numpy as np

import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

"""
# THE COMMENTD CODE IS RESPOSIBLE FOR CREATING JSON FILE FOR THE VOCABULARY

# Creating the vocabulary
train_dataframe = pd.read_csv('data/train.csv')
print("reading csv done")

to_lower = lambda x: str(x).lower()
train_questions1 = np.array(list(map(to_lower, train_dataframe.question1.values)))
train_questions2 = np.array(list(map(to_lower, train_dataframe.question2.values)))

print("loading questions done")
# CREATING THE VOCAB

question_1_counter = Counter()
for sent in train_questions1:
  question_1_counter.update(word_tokenize(sent))
question_1_vocab = len(question_1_counter)
print("counting done...")

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=question_1_vocab)
tokenizer.fit_on_texts(train_questions1)

indices = tokenizer.word_index
tokenizer_json = tokenizer.to_json()


# Create a json file for the vocab
print("creating tokenizer_json.json")
with open("data/tokenizer_json.json", 'w') as f:
    f.write(json.dumps(tokenizer_json, indent=2))
print("creating word_indices.json")
with open("data/word_indices.json", 'w') as f:
    f.write(json.dumps(indices, indent=2))

print("Done")
sys.exit(0)
"""

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




