import tweepy

from django.conf import settings

def get_twitter_api():
    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
    return tweepy.API(auth)
