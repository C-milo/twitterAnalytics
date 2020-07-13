import mongoengine

class Tweets(mongoengine.DynamicDocument):
    tweet_id = mongoengine.IntField(required=True, unique=True)
    username = mongoengine.StringField()
    location = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()
    hashtags = mongoengine.ListField(default='None')
    user_mentions = mongoengine.ListField()
    favorite_count = mongoengine.IntField()
    retweet_count = mongoengine.IntField()
    full_text = mongoengine.StringField()
    lang = mongoengine.StringField()
    quoted_user = mongoengine.StringField(default='None')
    quoted_mentions = mongoengine.StringField(default='None')
    quoted_text = mongoengine.StringField(default='None')
    quoted_url = mongoengine.StringField(default='None')
    media_title = mongoengine.StringField(default='None')    
    media_expanded_url = mongoengine.StringField(default='None')

class Config(mongoengine.Document):
    report_type = mongoengine.IntField(required=True)
    lookup_term = mongoengine.StringField(max_lenght=80, required=True)