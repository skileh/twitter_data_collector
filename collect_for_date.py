pip install git+https://github.com/tweepy/tweepy.git
  
import re
import tweepy
from datetime import datetime
from textblob import TextBlob
import json
import requests
import numpy as np
import pandas as pd

CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret
ACCESS_TOKEN = acess_token
ACCESS_TOKEN_SECRET = acess_token_secret

keyword = ('keyword')
count = 100

class TweetAnalyzer():

  def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
    '''
      Conectar com o tweepy
    '''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    


    self.conToken = tweepy.Client(barrer,auth)

  def __clean_tweet(self, tweets_text):
    '''
    Tweet cleansing.
    '''

    clean_text = re.sub(r'RT+', '', tweets_text) 
    clean_text = re.sub(r'@\S+', '', clean_text)  
    clean_text = re.sub(r'https?\S+', '', clean_text) 
    clean_text = clean_text.replace("\n", " ")

    return clean_text

  def search_by_keyword(self, keyword, count=100, result_type='mixed', lang='en', tweet_mode='extended'):
    '''
      Search for the twitters thar has commented the keyword subject.
    
    '''
    nome = self.conToken.get_user(username = keyword)
   # print(nome.data.id)
    print(nome)
    ID=nome.data.id
    tweets_iter = self.conToken.get_users_tweets(  
                                                   tweet_fields=['context_annotations', 'created_at'],
                                                   id=ID,
                                                   end_time ='2021-01-28T00:00:01Z' ,
                                                   start_time ='2018-07-28T00:00:01Z',
                                                   max_results=100
                                                )
    return tweets_iter.data

  def prepare_tweets_list(self, tweets_iter):
    '''
      Transforming the data to DataFrame.
    '''
   
    tweets_data_list = []
    for tweet in tweets_iter:
     # if not 'retweeted_status' in dir(tweet):
        tweets_data_list.append([tweet.id,tweet.text])
    #print(tweets_data_list)
    df = pd.DataFrame(tweets_data_list,columns=['id','text'])
    return df

analyzer = TweetAnalyzer(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, 
access_token = ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Para realizar as buscas usando a keyword e quantidade predefinida e converter em uma lista.
tweets_iter = analyzer.search_by_keyword(keyword, count)
tweets_list = analyzer.prepare_tweets_list(tweets_iter)
tweets_list.count()
