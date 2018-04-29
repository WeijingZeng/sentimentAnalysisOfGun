import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from textblob import TextBlob

tweets_data_path = './test-gun.txt'
tweets_file = open(tweets_data_path, "r")


def clean_tweet(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def sentiment(text):
    analysis=TextBlob(clean_tweet(text))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


tweets_text = []
tweets_sentiment = []
for line in tweets_file:
    try:
        tweet = json.loads(line)
        if tweet['text'] not in tweets_text:
            tweets_text.append(tweet['text'])
            tweets_sentiment.append(sentiment(tweet['text']))
    except:
        continue

tweets= pd.DataFrame([tweets_text,tweets_sentiment]).T
tweets.columns = ['tweet_text','tweet_sentiment']
print (tweets)
