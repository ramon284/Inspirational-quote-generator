# MachineLearningVu

## [Model 1](LSTM_Model_1/QuoteGenerator1.py)
Tutorial: [Tensorflow LSTM Text Generation](https://www.tensorflow.org/tutorials/text/text_generation)
*Note: Tensorflow has multiple different text generation tutorials*

**Language Representation:** Tokenisation of characters. Output by one-hot vector of characters.

**Quotes Representation:** Concatenated into large continious text

**Description:** This model currently uses all quotes as if it would be one big continuous text. Of course the quotes are separate contextual self-contained entities and not part of a continuous text. I.e. one quote has nothing to do with the next one. Currently not shuffling the quotes as a temporary solution to mitigate this. When all quotes about age are together and not shuffled at least the context in the big text is somewhat more appropriate. Have to link into how to provide data as separate self-contained text snippets. Will submit trained model after finished training.

**Notes:** Costumized training section of this tutorial is not incorporated.

**Current ETA:** 16 hours for 20 epochs (2019 MacBook i7 CPU)

**Some Predictions:** (15 Epochs) there's shall out of school where I started picketless.   Why not some of us seem to have a work of friends who tell you how terrible uncommon streesed view ideas of the governance - always everything. It needs to have to leave the world for meaningformed tools of life: the wind bllower and the Christmas playth the Republican Party.   I was always unstability, even if they must eat were the right, to the risks, but around the Christmas land, when the experience of most vegetables that meant you by the greatest politicians without get institcted, seriously. If a success is living nobody, you want more focus it's just loved to go to the seemed.   But the feminine genier where we ever have a Christmas relationship in one through alcoholics, and the Christmas Christmas.   Hate and low Mock or Here I passed out, so I can still have a Christmas skin or set and be as staying in investments. What do I'd have fone the Christmas, everyone is commonshing, candred, and to tell you: my generation

**Model Summary:** 

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

**Language Representation:** Tokenisation of words, internal embedding of words. Output by one-hot vector of words. 

**Quotes Representation:** Separate text sequences

**Description:** Unfinished work in progress. Current problem: LSTM to heavy to train on laptop. So porting to google Colab. Colab has to little RAM to do the sequence padding. Trying to pad on laptop, save data and open this data to train an LSTM in Colab.

**Notes:** -

**Current ETA:** -

**Some Predictions:** -

**Model Summary:**

 |Layer (type)    |             Output Shape      |        Param #   |
 | ------------- |:-------------:| -----:|
|embedding (Embedding)     |   (None, 89, 10)        |    340550    |
|lstm (LSTM)                |  (None, 100)           |    44400     |
|dropout (Dropout)          |  (None, 100)            |   0         |
|dense (Dense)              |  (None, 34055)          |   3439555   |
Total params: 3,824,505
Trainable params: 3,824,505
Non-trainable params: 0