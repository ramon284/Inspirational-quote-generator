import pandas as pd
import numpy as np
from collections import Counter
data = pd.read_csv('QuotesFiltered.csv')
pd.set_option('display.max_rows', None)


count = data.groupby(['GENRE']).count() 
#pd.set_option('display.max_rows', None) # to print all rows at once.
count=count.reset_index()
count.to_csv ('genreCount.csv', index = False, header=True)

wordCount = Counter(" ".join(data['QUOTE']).split()).most_common(500)
temp = pd.DataFrame(wordCount)
temp.columns = ['word','count']
print(temp)
temp.to_csv('wordCount.csv', index = False, header = True)





