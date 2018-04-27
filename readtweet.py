import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = './test-gun.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    ##print (line)
    try:
    ##line=tweets_file.readline();
    ##line=re.sub(r"(,?)(\w+?)\s+?:", r":\1'\2'",line)
        tweet = json.loads(line)
    ##print (tweet)
        tweets_data.append(tweet)
    except:
        continue

print (len(tweets_data))


# class TwitterClient(object):
#     def get_tweets(self):
#         tweets_data = []
#         tweets_file = open(tweets_data_path, "r")
#         for line in tweets_file:
#             try:
#                 tweet = json.loads(line)
#                 tweets_data.append(tweet)
#             except:
#                 continue
#         print (len(tweets_data))
#         tweets = []
#         for tweet in tweets_data:
#             parsed_tweet = {}
#             # saving text of tweet
#             parsed_tweet['text'] = tweet.text
#             # if tweet.retweet_count > 0:
#             #     # if tweet has retweets, ensure that it is appended only once
#             #     if parsed_tweet not in tweets:
#             #         tweets.append(parsed_tweet)
#             # else:
#             tweets.append(parsed_tweet)
#         return tweets
#
# def main():
#     api = TwitterClient()
#     tweets = api.get_tweets()
#     print (len(tweets))
#
# if __name__ == "__main__":
#     # calling main function
#     main()
