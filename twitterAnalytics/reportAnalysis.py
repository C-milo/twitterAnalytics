# Local libraries:
import json
#Third party libraries:
from pymongo import MongoClient
import pandas as pd
import numpy as np

class TwitterDB():
      def __init__(self):
            with open("mongodb_info.json", "r") as file:
                  creds = json.load(file)
            self.client = MongoClient(creds['HOSTNAME'], username=creds['USER'], password=creds['PASSWORD'], authSource=creds['DB_NAME'])
            self.db = self.client[creds['DB_NAME']] 
      def get_collection(self, collection_name):
            self.collection = self.db[collection_name]
            return self.collection

class TweetAnalyzer():
      def tweets_to_data_frame(self, tweets):
            df = pd.DataFrame(data=[tweet['text'] for tweet in tweets], columns=['Tweets'])
      
            df['id'] = np.array([tweet['id'] for tweet in tweets])
            df['len'] = np.array([len(tweet['text']) for tweet in tweets])
            df['date'] = np.array([tweet['created_at'] for tweet in tweets])
            df['date'] = df['date'].astype(str)
            df['source'] = np.array([tweet['source'] for tweet in tweets])
            df['likes'] = np.array([tweet['favorite_count'] for tweet in tweets])
            df['retweets'] = np.array([tweet['retweet_count'] for tweet in tweets])

            return df

def read_db_and_analyze(twitterUser):
      tweets = list()
      mongo_client = TwitterDB()
      twitter_analyzer = TweetAnalyzer()
      tweets_collection = mongo_client.get_collection(collection_name='tweets')

      for tweet in tweets_collection.find({"user.screen_name": twitterUser}):
            tweets.append(tweet)
      
      df = twitter_analyzer.tweets_to_data_frame(tweets)
      return df

def read_users_collection():      
      mongo_client = TwitterDB()
      users_collection = mongo_client.get_collection(collection_name='saved_users')
      query_dict = users_collection.find({'ref':'saved_users'}, {'username_list': 1})
      user_list = query_dict[0]['username_list']
      return user_list