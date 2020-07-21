#Local library
import json
#Third Party libraries
import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from pymongo import MongoClient
from mongoengine import connect, disconnect
#Custom library
from .model import Tweets
from .model import Config

class MongoDB():
      def db_connect(self):
            with open("twitterAnalytics/mongodb_info.json", "r") as file:
                  creds = json.load(file)
            connect(creds['DB_NAME'], host=creds['HOSTNAME'], username=creds['USER'], password=creds['PASSWORD'])            
            return print('connected to', creds['DB_NAME'])
      def get_reports(self):
            self.db_connect()
            response = []             
            for obj in Config.objects(): # pylint: disable=no-member
                  info = {
                        "rtype": obj.report_type,
                        "rname": obj.report_name
                  }
                  response.append(info)
            disconnect()            
            return response

class Configurator():
      def __init__(self, lword, reportType, numTweets=1):            
            MongoDB().db_connect()
            self.lword = lword
            self.numTweets = int(numTweets)
            self.reportType = int(reportType)
      def saveConfig(self):
            try:          
                  Config(
                        report_type = self.reportType,                                                       
                        report_name = self.lword
                  ).save()
                  msg = print('Configuration saved.')
            except: 
                  msg = print('Not saving config as it already exists.')
            return print(msg)
      def saveTweets(self, tweets):
            for tweet in tweets:                  
                  tw = Tweets(
                        tweet_id = tweet._json['id'],
                        search = self.lword,
                        username = tweet._json['user']['screen_name'],
                        location = tweet._json['user']['location'],
                        created_at = tweet._json['created_at'],
                        hashtags = tweet._json['entities']['hashtags'],
                        user_mentions = tweet._json['entities']['user_mentions'],
                        favorite_count = tweet._json['favorite_count'],
                        retweet_count = tweet._json['retweet_count'],
                        full_text = tweet._json['full_text'],
                        lang = tweet._json['lang']
                  )
                  if "quoted_status" in tweet._json:
                        print('tweet_id ', tweet._json['id'], 'is quoting someone')                        
                        tw.is_quoted = 'True'
                        tw.quoted_user = tweet._json['quoted_status']['user']['screen_name']
                        tw.quoted_text = tweet._json['quoted_status']['full_text']                                                   
                  else: pass                                    
                  if "retweeted_status" in tweet._json:
                        print('tweet_id ', tweet._json['id'], 'is retweeting someone')                        
                        tw.is_retweet = 'True'
                        tw.retweet_user = tweet._json['retweeted_status']['user']['screen_name']
                        tw.retweet_text =  tweet._json['retweeted_status']['full_text']
                        tw.retweet_id = tweet._json['retweeted_status']['id']
                  else: pass
                  if "extended_entities" in tweet._json:
                        print('tweet_id ', tweet._json['id'], 'has media')
                        tw.has_media = 'True'
                        if "dditional_media_info" in tweet._json:
                              tw.media_title = tweet._json['extended_entities']['media'][0]['additional_media_info']['title']
                        else: pass
                        tw.media_expanded_url = tweet._json['extended_entities']['media'][0]['expanded_url']
                  else: pass
                  print('saving tweet_id:', tweet._json['id'])
                  try:                         
                        tw.save()
                        print('saved tweet_id', tweet._json['id'])                                          
                  except:
                        print('skipping duplicate tweet_id', tweet._json['id'])
                        continue
            return print('Tweets saved.')
      def readParameters(self):
            switcher={
                  0: self.isHashtag,
                  1: self.isProfile
            }
            func = switcher.get(self.reportType)      
            return func()
      def isHashtag(self):            
            tc = TwitterClient(hashtag=self.lword)
            tweets = tc.get_hashtag_tweets(self.numTweets)            
            self.saveTweets(tweets)                              
            self.saveConfig()
            disconnect()
            return print('hashtag report can now be generated for',self.lword)
      def isProfile(self):
            tc = TwitterClient(user=self.lword)
            tweets = tc.get_user_timeline_tweets(self.numTweets)
            self.saveTweets(tweets)
            self.saveConfig()
            disconnect()
            return print('profile report can now be generated for ',self.lword)      
      
class TwitterAuthenticator():
      def authenticate_twitter_app(self):
            with open("twitterAnalytics/twitter_credentials.json", "r") as file:
                  creds = json.load(file)            
            auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
            auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
            return auth

class TwitterClient():
      def __init__(self, user=None, hashtag=''):
            self.auth = TwitterAuthenticator().authenticate_twitter_app()
            self.api = API(self.auth)
            self.user = user
            self.hashtag = hashtag + ' -filter:retweets'
      def get_api(self):
            return self.api
      def get_user_timeline_tweets(self, num_tweets):
            tweets = []
            for tweet in Cursor(self.api.user_timeline, id=self.user, tweet_mode="extended").items(num_tweets):
                  tweets.append(tweet)
            return tweets
      def get_hashtag_tweets(self, num_tweets):
            tweets = []
            for tweet in Cursor(self.api.search, q=self.hashtag, result_type="popular", tweet_mode="extended").items(num_tweets):                 
                  tweets.append(tweet)
            return tweets

# if __name__ == "__main__":
#       cf = Configurator(lword='#ElDiaMasFelizDeMiVida', reportType='0')
#       cf.readParameters()