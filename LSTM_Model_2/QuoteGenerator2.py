# 1. Import the libraries
# keras module for building LSTM 
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import keras.utils as ku 

# set seeds for reproducability
import tensorflow as tf
from numpy.random import seed
tf.random.set_seed(2)
seed(1)

import pandas as pd
import numpy as np
import string, os 

import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)

#2. Load the dataset
all_quotes = []
quotes_df = pd.read_csv("/Users/sethvanderbijl/Coding Projects/MachineLearningVu/Data/Data preprocessing/QuotesFiltered.csv", sep=";")

quotes_column = quotes_df["QUOTE"]

all_quotes.extend(list(quotes_column.values))

       

all_quotes = [h for h in all_quotes if h != "Unknown"]
print(len(all_quotes))


def clean_text(txt):
    txt = "".join(v for v in txt if v not in string.punctuation).lower()
    txt = txt.encode("utf8").decode("ascii",'ignore')
    return txt 

corpus = [clean_text(x) for x in all_quotes]
corpus[:10]

#3. Dataset preparation
#3.1 Cleaning
def clean_text(txt):
    txt = "".join(v for v in txt if v not in string.punctuation).lower()
    txt = txt.encode("utf8").decode("ascii",'ignore')
    return txt 

corpus = [clean_text(x) for x in all_quotes]
print(corpus[:10])

#3.2 Generating sequences of N-Gram tokens
tokenizer = Tokenizer()

def get_sequence_of_tokens(corpus):
    ## tokenization
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1
    
    ## convert data to sequence of tokens 
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    return input_sequences, total_words

inp_sequences, total_words = get_sequence_of_tokens(corpus)
print("\n\n We now have", len(inp_sequences), "Input sequences. First input sequences: \n",inp_sequences[:10])

# #3.3 Padding the Sequences and obtaining variables
def generate_padded_sequences(input_sequences):
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
    
    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
    label = ku.to_categorical(label, num_classes=total_words)
    return predictors, label, max_sequence_len

predictors, label, max_sequence_len = generate_padded_sequences(inp_sequences)
print(label, type(label), label[0],type(label[0]))

# del predictors
# del max_sequence_len
# del inp_sequences

with open('labels.npy', 'wb') as f:
    np.save(f, label)


# #4. Model
# def create_model(max_sequence_len, total_words):
#     input_len = max_sequence_len - 1
#     model = Sequential()
    
#     # Add Input Embedding Layer
#     model.add(Embedding(total_words, 10, input_length=input_len))
    
#     # Add Hidden Layer 1 - LSTM Layer
#     model.add(LSTM(100))
#     model.add(Dropout(0.1))
    
#     # Add Output Layer
#     model.add(Dense(total_words, activation='softmax'))

#     model.compile(loss='categorical_crossentropy', optimizer='adam')
    
#     return model

# model = create_model(max_sequence_len, total_words)
# model.summary()

# # #Train the Model
# model.fit(predictors, label, epochs=20, verbose=5)

# # #5. Generating texts
# def generate_text(seed_text, next_words, model, max_sequence_len):
#     for _ in range(next_words):
#         token_list = tokenizer.texts_to_sequences([seed_text])[0]
#         token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
#         predicted = model.predict_classes(token_list, verbose=0)
        
#         output_word = ""
#         for word,index in tokenizer.word_index.items():
#             if index == predicted:
#                 output_word = word
#                 break
#         seed_text += " "+output_word
#     return seed_text.title()