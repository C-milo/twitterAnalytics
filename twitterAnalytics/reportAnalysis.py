# Local libraries:
# Third party libraries:
import pandas as pd
import numpy as np
# Custom Libraries:
from .reportConfig import MongoDB
from .model import Tweets

# Hashtag is 0
# Profile is 1

def analyze(rtype, rname):
      if rtype == '0':
            print('Running analysis for a hashtag report')
      elif rtype == '1':
            print('Running analysis for a profile report')            
      else: pass
      return None

class TweetAnalyzer():
      def __init__(self, rname):
            MongoDB().db_connect()
            self.rname = rname      
      def tweets_to_df(self):            
            db_response = Tweets.objects(search=self.rname) # pylint: disable=no-member
            df = pd.DataFrame(data=[tweet.tweet_id for tweet in db_response], columns=['tweet_id'])
            df['report_name'] = np.array([tweet.search for tweet in db_response]) 
            df['location'] = np.array([tweet.location for tweet in db_response])
            df['created_at'] = np.array([tweet.created_at for tweet in db_response])
            df['favorite_count'] = np.array([tweet.favorite_count for tweet in db_response])
            df['retweet_count'] = np.array([tweet.retweet_count for tweet in db_response])
            df['lenght_text'] = np.array([len(tweet.full_text) for tweet in db_response])
            df['language'] = np.array([tweet.lang for tweet in db_response])
            df['is_quote'] = np.array([tweet.lang for tweet in db_response])
            return df                  
            