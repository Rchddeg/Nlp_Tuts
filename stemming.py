'''
Purpose of stemming. To ensure variations of a verb in terms of tense all go back to the sme thing to help in decoding the meaning of a sentence
example of stemmers...brown stemmer, porter stemmer, snowball stemmer
'''
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
example_words=['python','pythoner','pythoning','pythoned']
for w in example_words:
    print(ps.stem(w))