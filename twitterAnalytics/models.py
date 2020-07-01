import mongoengine

class Tweet(mongoengine.DynamicDocument):
    tweet_id = mongoengine.IntField(required=True, unique=True)
    username = mongoengine.StringField()
    location = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()
    hashtags = mongoengine.ListField()
    user_mentions = mongoengine.ListField()
    favorite_count = mongoengine.IntField()
    retweet_count = mongoengine.IntField()
    full_text = mongoengine.StringField()
    lang = mongoengine.StringField()
    quoted_user = mongoengine.StringField()
    quoted_mentions = mongoengine.ListField()
    quoted_text = mongoengine.StringField()
    quoted_url = mongoengine.StringField()
    media_title = mongoengine.StringField()
    media_image_url = mongoengine.StringField()
    media_expanded_url = mongoengine.StringField()

class Config(mongoengine.Document):
    report_type = mongoengine.StringField(required=True)
    lookup_term = mongoengine.StringField(max_lenght=80, required=True)