import pandas as pd

df = pd.read_csv("Quotes.txt", sep=";")

# df = df.sample(frac=1).reset_index(drop=True)


print(df.head(10))

with open('output.txt', 'w') as f:
    f.write(df['QUOTE'].str.cat(sep='\n'))