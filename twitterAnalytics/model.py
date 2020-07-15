import mongoengine

class Tweets(mongoengine.DynamicDocument):
    tweet_id = mongoengine.IntField(unique=True)
    username = mongoengine.StringField()
    location = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()
    hashtags = mongoengine.ListField()
    user_mentions = mongoengine.ListField()
    favorite_count = mongoengine.IntField()
    retweet_count = mongoengine.IntField()
    full_text = mongoengine.StringField()
    lang = mongoengine.StringField()
    #Is quoted    
    is_quoted = mongoengine.StringField(default='False')
    quoted_user = mongoengine.StringField(default='None')    
    quoted_text = mongoengine.StringField(default='None')    
    #Is Retweet
    is_retweet = mongoengine.StringField(default='False')
    retweet_text = mongoengine.StringField()
    retweet_id = mongoengine.IntField()
    retweet_user = mongoengine.StringField(default='None')    
    #Has Media
    has_media = mongoengine.StringField(default='False') 
    media = mongoengine.DictField()

class Config(mongoengine.Document):
    report_type = mongoengine.IntField(required=True)
    lookup_term = mongoengine.StringField(max_lenght=80, required=True, unique=True)