import re
import tweepy
from datetime import datetime
from textblob import TextBlob

CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret
ACCESS_TOKEN = acess_token
ACCESS_TOKEN_SECRET = acess_token_secret

keyword = ("beyonce")
count = 10

class TweetAnalyzer():

  def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
    '''
      Conectar com o tweepy
    '''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    


    self.conToken = tweepy.Client(auth)

  def __clean_tweet(self, tweets_text):
    '''
    Tweet cleansing.
    '''

    clean_text = re.sub(r'RT+', '', tweets_text) 
    clean_text = re.sub(r'@\S+', '', clean_text)  
    clean_text = re.sub(r'https?\S+', '', clean_text) 
    clean_text = clean_text.replace("\n", " ")

    return clean_text

  def search_by_keyword(self, keyword, count=10, result_type='mixed', lang='en', tweet_mode='extended'):
    '''
      Search for the twitters thar has commented the keyword subject.
    '''
    ID = self.conToken.get_user(username =keyword)
    tweets_iter = self.conToken.get_users_tweets(
                                                   id=ID,
                                                   end_time =datetime(2020,1,31,0,0,0).date() ,
                                                   start_time =datetime(2019,7,31,0,0,0).date(),
                                                   max_results=count
                                                   )

    return tweets_iter

  def prepare_tweets_list(self, tweets_iter):
    '''
      Transforming the data to DataFrame.
    '''

    tweets_data_list = []
    for tweet in tweets_iter:
      if not 'retweeted_status' in dir(tweet):
        tweet_text = self.__clean_tweet(tweet.full_text)
        tweets_data = {
            'len' : len(tweet_text),
            'ID' : tweet.id,
            'User' : tweet.user.screen_name,
            'UserName' : tweet.user.name,
            'UserLocation' : tweet.user.location,
            'TweetText' : tweet_text,
            'Language' : tweet.user.lang,
            'Date' : tweet.created_at,
            'Source': tweet.source,
            'Likes' : tweet.favorite_count,
            'Retweets' : tweet.retweet_count,
            'Coordinates' : tweet.coordinates,
            'Place' : tweet.place 
        }

        tweets_data_list.append(tweets_data)

    return tweets_data_list

analyzer = TweetAnalyzer(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, 
access_token = ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Para realizar as buscas usando a keyword e quantidade predefinida e converter em uma lista.
tweets_iter = analyzer.search_by_keyword(keyword, count)
tweets_list = analyzer.prepare_tweets_list(tweets_iter)
print(tweets_list)
