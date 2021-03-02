# MachineLearningVu

## [Model 1](LSTM_Model_1/QuoteGenerator1.py)
Tutorial: [Tensorflow LSTM Text Generation](https://www.tensorflow.org/tutorials/text/text_generation)
*Note: Tensorflow has multiple different text generation tutorials*

**Language Representation:** Tokenisation of characters

**Quotes Representation:** Concatenated into large continious text

**Description:** This model currently uses all quotes as if it would be one big continuous text. Of course the quotes are separate contextual self-contained entities and not part of a continuous text. I.e. one quote has nothing to do with the next one. Currently not shuffling the quotes as a temporary solution to mitigate this. When all quotes about age are together and not shuffled at least the context in the big text is somewhat more appropriate. Have to link into how to provide data as separate self-contained text snippets. Will submit trained model after finished training.

**Notes:** Costumized training section of this tutorial is not incorporated.

**Current ETA:** 16 hours for 20 epochs (2019 MacBook i7 CPU)

**Some Predictions:** -

**Mode Summary:** 

|Layer (type)     |            Output Shape |             Param #   |
| ------------- |:-------------:| -----:|
embedding (Embedding)     |   multiple       |           21248     
gru (GRU)      |              multiple       |           3938304   
dense (Dense)      |          multiple      |            85075     

Total params: 4,044,627

Trainable params: 4,044,627

Non-trainable params: 0


## [Model 2](LSTM_Model_2/QuoteGenerator2.py)
Tutorial: [Kaggle Beginners Text Generation](https://www.kaggle.com/shivamb/beginners-guide-to-text-generation-using-lstms)

**Language Representation:** Tokenisation of words

**Quotes Representation:** Separate text sequences

**Description:** Unfinished work in progress

**Notes:** -

**Current ETA:** -

**Some Predictions:** -