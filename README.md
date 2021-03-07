# MachineLearningVu

## [Model 1](LSTM_Model_1/QuoteGenerator1.py)
Tutorial: [Tensorflow LSTM Text Generation](https://www.tensorflow.org/tutorials/text/text_generation)
*Note: Tensorflow has multiple different text generation tutorials*

**Language Representation:** Tokenisation of characters. Output by one-hot vector of characters.

**Quotes Representation:** Concatenated into large continious text

**Description:** This model currently uses all quotes as if it would be one big continuous text. Of course the quotes are separate contextual self-contained entities and not part of a continuous text. I.e. one quote has nothing to do with the next one. Currently not shuffling the quotes as a temporary solution to mitigate this. When all quotes about age are together and not shuffled at least the context in the big text is somewhat more appropriate. Have to link into how to provide data as separate self-contained text snippets. Will submit trained model after finished training.

**Notes:** Costumized training section of this tutorial is not incorporated.

**Current ETA:** 16 hours for 20 epochs (2019 MacBook i7 CPU), 1.5 hour for 20 epochs on Colab Nvidia Tesla k-80

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

**Description:** Unfinished work in progress. Can't fit whole dataset at once into the model.

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


## [Model 3](LSTM_Model_3/LSTM-model-3.ipynb)
Tutorial: [Generating Quotes using LSTM](https://www.kaggle.com/hariharanhd/generating-quotes)

**Language Representation:** Tokenization of words. Uses the current sentence as input, next word as label which is a one-hot-vector.

**Description:** This model was trained with a total of 36k quotes. This is because all quotes that were multi-sentence were dropped, as well as duplicate ones. After the input sequence was created, this sequence was split into 10 seperate chunks. The model was then trained 10 seperate times for 25 epochs, taking roughly ~15 minutes per chunk on a google colab GPU. Since the input was split into 10 parts, some chunks might end with an unfinished sentence while the next starts with one that's already half-completed. This should not be a problem since it only happens a max. of 10 times while training 36k quotes. Quotes were also not shuffled, not sure if that would make a difference. 

What is also worth pointing out is that this generator basically just generates long pieces of text, based on an input of how long you want the text to be.
It might be an idea to use a grammar-checker on the generated piece of text until we find the most grammatically correct sentence inside of our long text string.


**Notes:** Training chunks in a for-loop gives memory crashes, even when clearing all used variables. Training a model in chunks like this required a bunch of manual resets of the notebook. If we cannot find a way around this then char-based models might be much easier to train.

**Some Predictions:** Here, model 2 is the fully trained one, whereas model 1 is trained on a smaller dataset.

| Model | Quote |
|---------|---------------------------------------------------------------------------------|
| Model 1 | Time in the see want to not wise we the very tender and will poet of. |     
| Model 2 | Time is the truth that is the truth that all the time is the most important to. |
| Model 1 | Friendship on one not a become cool man of quite a become way of from more programming a adore reach be.|
| Model 2 | Friendship is a fool to know the truth and another is not a fool to know the truth and yet he.|
| Model 1 | Passion while not the gathering defend and ourselves to also a architecture disappointment in that modern in I the secret and the almost and.|
| Model 2 | Passion is a weapon of the war of fighting vanguard has created in its war and customers and advanced technology and the same tasks.|

**Model Summary:**

|Layer (type)     |            Output Shape |             Param #   |
| ------------- |:-------------:| -----:|
embedding (Embedding) | (None, 80, 64) | 1549568 |
lstm (LSTM) | (None, 64) |  33024 |
dense (Dense) | (None, 24212) | 1573780 |


Total params: 3,156,372

Trainable params: 3,156,372

Non-trainable params: 0

