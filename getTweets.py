from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
consumer_key = 'qEoOOWuiXFIDI3l8ORWO6xGZh'
consumer_secret = 'O0Po83fDyTF0PebqpFPoB2dKgc5HtuytlWb9l5hoXv9D8GROZP'
access_token = '982758745011904513-uRNlhxiZYogeInmByrJIX3oTyFKqoRm'
access_token_secret = 'chZMVxofGuAvvpuy1MNGskIrpJH4y2KFVAVetrIg5F5qT'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'gun control'
    stream.filter(track=['gun control'])
