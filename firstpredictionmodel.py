# -*- coding: utf-8 -*-
"""firstpredictionmodel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13uybf_h5iYoNeSTyudGSwZ4dj5lwRVaU
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
import string
import requests

response = requests.get('https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')

response.text

data = response.text.split('\n')
data = data[253:]
data[0]

len(data)

data = " ".join(data)

# Removing Punctuations

def clean_data(doc):
  tokens = doc.split()
  table = str.maketrans('', '', string.punctuation)
  tokens = [ w.translate(table) for w in tokens ]
  tokens = [word for word in tokens if word.isalpha()]
  tokens = [word.lower() for word in tokens]
  return tokens

tokens = clean_data(data)
print(tokens[:50])
# len(tokens) #len(set(tokens))

length = 50 + 1  #input + output length
lines = []
for i in range(length, len(tokens)):
  seq = tokens[i-length:i]
  line = ' '.join(seq)
  lines.append(line)
  if i > 200000:
    break
# print(len(lines))

"""## LSTM Model and prepare x and y

"""

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines) 
sequences = tokenizer.texts_to_sequences(lines) # Assigning every unique word to integer Text->Integer

sequences = np.array(sequences) # Integers -> Arrays
x,y = sequences[ : ,  :-1], sequences[ : ,-1] # x-> All 50 columns(Not 51) and rows & y-> All rows & Last column(51)
# x[0], y[0]

vocab_size = len(tokenizer.word_index) + 1  
# print(vocab_size)
y = to_categorical(y,num_classes=vocab_size)
seq_length = x.shape[1]

"""## LSTM Model"""

model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))  # Embedding Layer
model.add(LSTM(100, return_sequences=True)) # 1st LSTM layer with 100 hidden layers
model.add(LSTM(100)) # 2nd LSTM layer with 100 hidden layers
model.add(Dense(100, activation='relu'))  #Dense layer with 100 neurons and relu activation
model.add(Dense(vocab_size, activation='softmax')) #Probability for each predicted word

model.summary() #State of model

# optimizers shape and mold your model into its most accurate possible form by futzing with the weights
model.compile(loss="categorical_crossentropy", optimizer= 'adam', metrics=['accurancy'])

# Training
model.fit(x, y, batch_size=256, epochs=100) # 500 epochs for better accuracy

# Prediction
seed_text=lines[12343]
def generate_text_seq(model, tokenizer, text_seq_length, seed_text, n_words):
  text=[]
  for _ in range(n_words):
    encoded = tokenizer.texts_to_sequences([seed_text])[0]
    encoded = pad_sequences(encoded, maxlen =text_seq_length, truncating='pre') # truncating to fix length

    y_predict = model.predict_classes(encoded) # Prediction of Index
    predicted_word = ' '
    # Finding word of predicted index 
    for word,index in tokenizer.word.index.items():        
      if index == y_predict:
        predicted_word = word
        break
    seed_text = seed_text  + ' ' + predicted_word
    text.append(predicted_word)
  return ' '.join(text)
#Prediction
generate_text_seq(model, tokenizer, seq_length, seed_text, 100)