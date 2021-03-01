import pandas as pd
import numpy as np
data = pd.read_csv('output.csv')
pd.set_option('display.max_rows', None)


count = data.groupby(['GENRE']).count() 
#pd.set_option('display.max_rows', None) # to print all rows at once.
count=count.reset_index()
count.to_csv ('genreCount.csv', index = False, header=True)

Counter(" ".join(data['QUOTE']).split()).most_common(100) ## counts 100 most common words




