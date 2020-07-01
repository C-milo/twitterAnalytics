#Local library
import json
#Third Party libraries
import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from pymongo import MongoClient
from mongoengine import connect
#Custom library
from models import Tweet
from models import Config

# class TwitterDB():
#       def __init__(self):
#             with open("mongodb_info.json", "r") as file:
#                   creds = json.load(file)
#             self.client = MongoClient(creds['HOSTNAME'], username=creds['USER'], password=creds['PASSWORD'], authSource=creds['DB_NAME'])
#             self.db = self.client[creds['DB_NAME']] 
#       def get_collection(self, collection_name):
#             self.collection = self.db[collection_name]
#             return self.collection

def db_connect():
      with open("mongodb_info.json", "r") as file:
            creds = json.load(file)
      connect(creds['DB_NAME'], host=creds['HOSTNAME'], username=creds['USER'], password=creds['PASSWORD'])            
      return print('connected to', creds['DB_NAME'])

class TwitterAuthenticator():
      def authenticate_twitter_app(self):
            with open("twitter_credentials.json", "r") as file:
                  creds = json.load(file)            
            auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
            auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
            return auth

class TwitterClient():
      def __init__(self, user=None):
            db_connect()
            self.auth = TwitterAuthenticator().authenticate_twitter_app()
            self.api = API(self.auth)
            self.user = user
      def get_user_timeline_tweets(self, num_tweets):
            tweets = []
            for tweet in Cursor(self.api.user_timeline, id=self.user, tweet_mode="extended").items(num_tweets):
                  tweets.append(tweet)
            return tweets



# 
# class TweetAnalyzer():
#       def tweets_to_data_frame(self, tweets):
#             df = pd.DataFrame(data=[tweet['text'] for tweet in tweets], columns=['Tweets'])      
#             df['id'] = np.array([tweet['id'] for tweet in tweets])
#             df['len'] = np.array([len(tweet['text']) for tweet in tweets])
#             df['date'] = np.array([tweet['created_at'] for tweet in tweets])
#             df['date'] = df['date'].astype(str)
#             df['source'] = np.array([tweet['source'] for tweet in tweets])
#             df['likes'] = np.array([tweet['favorite_count'] for tweet in tweets])
#             df['retweets'] = np.array([tweet['retweet_count'] for tweet in tweets])
#             return df
# 
# def run_search(twitterUser, save_user):
#       user = twitterUser
#       twitter_client = TwitterClient()
#       mongo_client = TwitterDB()
# 
#       api = twitter_client.get_twitter_client_api()
#       try:
#             tweets = api.user_timeline(screen_name=user, count=10)
#       except:
#             return -1
      
#       if save_user  == "True":
#             print('save_user set to True, saving user in users_collection')
#             users_collection = mongo_client.get_collection(collection_name='saved_users')
#             users_collection.update({'ref':'saved_users'}, {'$addToSet': {'username_list': user}})
#       else:
#             None
#       #Inserts tweets into MongoDB tweets_collection
#       tweets_collection = mongo_client.get_collection(collection_name='tweets')
#       for t in tweets:
#             try:                  
#                   tweets_collection.update(t._json, t._json, upsert=True)
#                   print('tweets_collection db updated')
#             except:
#                   print('skipping duplicated id')
#       return
# 
# def read_db_and_analyze(twitterUser):
#       tweets = list()
#       mongo_client = TwitterDB()
#       twitter_analyzer = TweetAnalyzer()
#       tweets_collection = mongo_client.get_collection(collection_name='tweets')
#       #Look up in DB for username tweets
#       for tweet in tweets_collection.find({"user.screen_name": twitterUser}):
#             tweets.append(tweet)
#       #Stores tweets in dataframe
#       df = twitter_analyzer.tweets_to_data_frame(tweets)
#       return df

# def read_users_collection():      
#       mongo_client = TwitterDB()
#       users_collection = mongo_client.get_collection(collection_name='saved_users')
#       query_dict = users_collection.find({'ref':'saved_users'}, {'username_list': 1})
#       user_list = query_dict[0]['username_list']
#       return user_list