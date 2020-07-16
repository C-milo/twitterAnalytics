# Local libraries:
import json
#Third party libraries:
import pandas as pd
import numpy as np
#Custom Libraries:
from twitterAnalytics.reportConfig import MongoDB
from twitterAnalytics.model import Tweets

class TweetAnalyzer():
      def __init__(self, reportName):
            MongoDB().db_connect()
            self.reportName = reportName      
      def tweets_to_df(self):            
            db_response = Tweets.objects(search=self.reportName) # pylint: disable=no-member
            df = pd.DataFrame(data=[tweet.tweet_id for tweet in db_response], columns=['Tweet_ID'])
            df['report_name'] = np.array([tweet.search for tweet in db_response]) 
            df['location'] = np.array([tweet.location for tweet in db_response])
            df['created_at'] = np.array([tweet.created_at for tweet in db_response])
            df['favorite_count'] = np.array([tweet.favorite_count for tweet in db_response])
            df['retweet_count'] = np.array([tweet.retweet_count for tweet in db_response])
            df['lenght_text'] = np.array([len(tweet.full_text) for tweet in db_response])
            df['language'] = np.array([tweet.lang for tweet in db_response])
            df['is_quote'] = np.array([tweet.lang for tweet in db_response])
            return df                  
            