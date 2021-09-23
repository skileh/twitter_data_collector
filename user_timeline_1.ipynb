import tweepy
import asyncio
import re

consumer_key = "your_key"
consumer_secret = "your_secret"
acess_token = "your_token"
acess_token_secret = "your_secret_token"

#OAuthHandler is responsible for authenticating twitter
authentication = tweepy.OAuthHandler(consumer_key,consumer_secret)
#assignment of access token values
authentication.set_access_token(acess_token,acess_token_secret)

api = tweepy.API(authentication)

#conecting to twitter
twitter = tweepy.API(authentication)
def capture(user, limit):
	resultados = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
	tweets = [] 
	for r in resultados:
		# uses regular expression to remove URL from tweet
		# http gets the beginning of the url
		# \S+ gets non-white characters (the end of the URL)
		tweet = re.sub(r'http\S+', '', r.full_text)
		tweets.append(tweet.replace('\n', ' ')) # add in the list
	return tweets 

#print the values
tweets = capture(usuario='jairbolsonaro', limite=10)
print(tweets)
