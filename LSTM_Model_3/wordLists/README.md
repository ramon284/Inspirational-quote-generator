This map contains some files which help the model choose a starting point and also filter out some potentially bad results.

The document "illegalWordsList.txt" contains words a sentence should not end with, for example "an" or "the". 
If a generated quote ends with one of these words then the word simply gets deleted and we'll check again if the last word is now legal.

Example: "Be good to people for no reason an the." -> "Be good to people for no reason an." -> "Be good to people for no reason."

The other text files here represent categories, and contain starting words for each category. This makes it easy to choose what kind of quote you want to generate. 
Currently the model randomly selects a file and then randomly picks a word inside this file to start a quote. You can also easily give a user the option to choose a category.
