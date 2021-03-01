import pandas as pd
import numpy as np
data = pd.read_csv('quotesRaw.csv', sep=';')


print(f"Total Quotes: {data.shape}")
print('----------------------------------------------')
genres = data['GENRE'].drop_duplicates()
print(genres.shape) ## 117 unique genres

print('----------------------------------------------')
authors = data['AUTHOR'].drop_duplicates()
print(authors.shape) ## 11174 unique authors
print('----------------------------------------------')
quotes = data['QUOTE'].drop_duplicates()
print(f"Total Unique Quotes: {quotes.shape}")
print(quotes)



quotesWithGenre = data.drop(columns=['AUTHOR'])
print(quotesWithGenre[:5])
print(quotesWithGenre.shape)
quotesWithGenre.drop_duplicates('QUOTE', inplace=True)
print(quotesWithGenre.shape)


quotesWithGenre.to_csv ('QuotesFiltered.csv', index = False, header=True)





