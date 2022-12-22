import api_keys
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]: +', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)

    return text

def getSubjectivity(text):
    return round(TextBlob(text).sentiment.subjectivity, 4)

def getPolarity(text):
    return round(TextBlob(text).sentiment.polarity, 4)

client = tweepy.Client(bearer_token=api_keys.BEARER_TOKEN)

query = 'liverpool fc transfer news lang:en'
#raw_tweets = client.get_users_tweets(id='343627165', max_results=10)
raw_tweets = client.search_recent_tweets(query=query, max_results=50)
clean_tweets = []

for tweet in raw_tweets.data:
    clean_tweet = cleanText(str(tweet))
    clean_tweets.append(clean_tweet)
    print(clean_tweet, getSubjectivity(clean_tweet), getPolarity(clean_tweet), '\n')

allWords = ' '.join([twts for twts in clean_tweets])
wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)

plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis('off')
plt.show()