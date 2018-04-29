import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = './test-gun.txt'
tweets_text = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        if tweet['text'] not in tweets_text:
            tweets_text.append(tweet['text'])
    except:
        continue

tweets= pd.DataFrame([tweets_text]).T
print (tweets)
