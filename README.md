# twitterAnalytics
For fun and education. 

This is a work in progress. 

# Technologies used in this webapp:

Python.
JavaScript
Dash
Flask
MongoDB (mongoengine)
Tweepy

See requirements.txt for all python libraries.

# Running the app:

Two JSON files must be created to setup tweepy and mongodb connections:

mongodb_info.json:
```json
{
      "HOSTNAME": "<HOSTNAME>",
      "DB_NAME": "<DB-NAME>",      
      "USER": "<USER>",
      "PASSWORD": "<PASSWORD>"
}
```

twitter_credentials.json:
```json
{
      "CONSUMER_KEY": "<CONSUMER_KEY>",
      "CONSUMER_SECRET": "<CONSUMER_SECRET>",
      "ACCESS_TOKEN": "<ACCESS_TOKEN>",
      "ACCESS_SECRET": "<ACCESS_SECRET>"
}
```
