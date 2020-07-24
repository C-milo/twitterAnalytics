# Local libraries:
# Third party libraries:
import pandas as pd
import numpy as np
# Custom Libraries:
from .reportConfig import MongoDB
from .model import Tweets

# Hashtag is 0
# Profile is 1

class TweetAnalyzer():
      def __init__(self, kword, rtype):
            MongoDB().db_connect()
            self.kword = kword
            self.rtype = rtype
      def analyze(self):
            if self.rtype == '0':
                  print('Running analysis for a hashtag report')
                  self.create_multiuse_df()
            elif self.rtype == '1':
                  print('Running analysis for a profile report')
                  self.create_multiuse_df()
            else: pass
            return None      
      def create_multiuse_df(self):            
            db_response = Tweets.objects(key_word=self.kword) # pylint: disable=no-member
            df = pd.DataFrame(data=[tweet.tweet_id for tweet in db_response], columns=['tweet_id'])
            df['key_word'] = np.array([tweet.key_word for tweet in db_response])
            df['username'] = np.array([tweet.username for tweet in db_response])
            df['location'] = np.array([tweet.location for tweet in db_response])
            df['created_at'] = np.array([tweet.created_at for tweet in db_response])
            df['favorite_count'] = np.array([tweet.favorite_count for tweet in db_response])
            df['retweet_count'] = np.array([tweet.retweet_count for tweet in db_response])
            df['lenght_text'] = np.array([len(tweet.full_text) for tweet in db_response])
            df['language'] = np.array([tweet.lang for tweet in db_response])
            df['is_quote'] = np.array([tweet.is_quoted for tweet in db_response])
            df['quoted_user'] = np.array([tweet.quoted_user for tweet in db_response])
            df['is_retweet'] = np.array([tweet.is_retweet for tweet in db_response])
            df['retweet_id'] = np.array([tweet.retweet_id for tweet in db_response])
            df['retweet_user'] = np.array([tweet.retweet_user for tweet in db_response])
            df['has_media'] = np.array([tweet.has_media for tweet in db_response])
            self.create_csv(df=df, table_name='multiuse')
            return None
      def create_csv(self, df, table_name):
            path_to_file = './twitterAnalytics/plotydash/data/' + self.rtype + '/'
            file_name = self.kword + '_' + table_name + '.csv'
            full_name = path_to_file + file_name
            df.to_csv(full_name, index=False)
            return None
      