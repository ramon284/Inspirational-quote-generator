# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:24:01 2021

@author: diego
"""

import matplotlib.pyplot as plt
import pandas as pd
import spacy
from collections import Counter
from wordcloud import WordCloud

data = pd.read_csv('output.csv')
pd.set_option('display.max_rows', None)


count = data.groupby(['GENRE']).count() 
#pd.set_option('display.max_rows', None) # to print all rows at once.
count=count.reset_index()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
limit = 10
ax.pie(count.QUOTE[:limit], labels = count.GENRE[:limit],autopct='%1.2f%%')
plt.savefig('piechart.png', dpi=250)
plt.show()



text = data.QUOTE.str.cat()[:100000]


nlp = spacy.load("en_core_web_sm")
doc = nlp(text)


# words = [token.text
#           for token in doc
#           if not token.is_stop and not token.is_punct]

wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud.png', dpi=250)
plt.show()


nouns = [token.lemma_
          for token in doc
          if (not token.is_stop and
              not token.is_punct and
              token.pos_ == "NOUN")]

verbs = [token.lemma_
          for token in doc
          if (not token.is_stop and
              not token.is_punct and
              token.pos_ == "VERB")]

adjectives = [token.lemma_
          for token in doc
          if (not token.is_stop and
              not token.is_punct and
              token.pos_ == "ADJ")]
