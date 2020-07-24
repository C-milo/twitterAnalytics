import mongoengine as me

class Tweets(me.DynamicDocument):
    tweet_id = me.IntField(unique=True)
    key_word = me.StringField(required=True)
    username = me.StringField()
    location = me.StringField()
    created_at = me.DateTimeField()
    hashtags = me.ListField()
    user_mentions = me.ListField()
    favorite_count = me.IntField()
    retweet_count = me.IntField()
    full_text = me.StringField()
    lang = me.StringField()
    #Is quoted    
    is_quoted = me.StringField(default='False')
    quoted_user = me.StringField(default='None')    
    quoted_text = me.StringField(default='None')    
    #Is Retweet
    is_retweet = me.StringField(default='False')
    retweet_text = me.StringField(default='None')
    retweet_id = me.IntField()
    retweet_user = me.StringField(default='None')    
    #Has Media
    has_media = me.StringField(default='False') 
    media = me.DictField()

class Config(me.Document):    
    report_type = me.IntField(required=True)
    key_word = me.StringField(max_lenght=80, required=True, unique=True)