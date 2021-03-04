import pandas as pd
import keras
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import keras.utils as ku

data = pd.read_csv('QuotesFiltered.csv', sep=";")

tokenizer = tf.keras.preprocessing.text.Tokenizer( ##standard tf tokenizer 
    num_words=None,
    filters='!"#$%&()*+<=>?@[\\]^_`{|}~\t\n', ## Regex baby (Might have to add some arguments)
    lower=True, split=' ', char_level=False, oov_token=None
)

def generate_sequences(corpus): 
    tokenizer.fit_on_texts(corpus) ## create a token for every unique word
    total_words = len(tokenizer.word_index) + 1
    print(f"Total unique words in the text corpus: {total_words}")
    input_sequences = []
    for line in corpus:
        seq = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(seq)):
            ngram_seq = seq[:i+1]
            input_sequences.append(ngram_seq)
            
    return input_sequences, total_words ##input sequence is an array of tokenized words, increasing one word per row

input_sequences, total_words = generate_sequences(data)
	
def generate_input_sequence(input_sequences): ##Generates arrays for predictors and labels
    maxlen = max([len(x) for x in input_sequences])
    input_sequences = pad_sequences(input_sequences, maxlen=maxlen)
    predictors, label = input_sequences[:, :-1], input_sequences[:, -1]
    label = ku.to_categorical(label, num_classes=total_words) ##Labels are one-hot vectors, and represent the next word to come after the input sequence row
    return predictors, label, maxlen

predictors, label, maxlen = generate_input_sequence(input_sequences)





##--------------------------  Some other stuff  -------------------------------------##
data = data.drop(data[data.QUOTE.str.count("\.") > 1].index) ## filters quotes with more than 1 dot (multiple sentence quotes)
                                            ## This might help our model by keeping the quote structure uniform and simple

data = data['QUOTE'].str.lower() ##makes all strings lowercase
data = data.str.capitalize() ##capitalizes first words, might be useful after using str.lower()
##-----------------------------------------------------------------------------------##
