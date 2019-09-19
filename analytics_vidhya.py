import re    # for regular expressions
import nltk  # for text manipulation
import string
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer, WordNetLemmatizer

# racist/ sexist tweets are labelled with 1 else, 0
train  = pd.read_csv('datasets/train_E6oV3lV.csv')
test = pd.read_csv('datasets/test_tweets_anuFYb8.csv')
train.set_index("id")
# check out some tweets from both classes
print(f' NON RACIST?SEXIST Tweets>>>>{train[train["label"] == 0].head()}')
print(f' Racist/sexist tweets {train[train["label"] == 1].head()}')
# inspect label distribution
print(train["label"].value_counts())

# visualize label distribution
sns.countplot(train["label"])
plt.title("Label Distribution")
plt.show()

# check distribution in terms of length of tweets in the train and test set
length_train = train['tweet'].str.len()
length_test = test['tweet'].str.len()
print(length_train)
plt.hist(length_train, bins=20, label="train_tweets")
plt.hist(length_test, bins=20, label="test_tweets")
plt.legend()
plt.show()

# combine train and test for data processing
combined = train.append(test, ignore_index=True)
print(combined.shape)

# data cleaning function to remove any pattern
def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt) # substitute pattern with blank
    return input_txt

'''
Tweet cleaning steps
1. Remove twitter handles since they dont add to the sentiment of the tweet(denoted by @user due to privacy)
2. Remove punctuation numbers and special characters
3. Remove short words of size 3 or less. They dont have much lexical meaning.
(Maybe, will run model with and without this step to view difference)
4. Normalize text data. eg stemming
'''
combined['tidy_tweet'] = np.vectorize(remove_pattern)(combined['tweet'], "@[\w]*")
combined['tidy_tweet'] = combined['tidy_tweet'].str.replace("[^a-zA-Z#]", " ") # replace everything except letters and #
combined['tidy_tweet'] = combined['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

# Normalization
tokenized_tweet = combined['tidy_tweet'].apply(lambda x: x.split()) # tokenizing
print(tokenized_tweet.head())

stemmer = PorterStemmer()
lemmetizer = WordNetLemmatizer() # will consider in terms of accuracy of final model

tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
# stitch items back together
for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])
combined['tidy_tweet'] = tokenized_tweet
print(combined.head())