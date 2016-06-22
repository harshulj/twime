import tweepy
import operator
from datetime import datetime, time

from django.utils import timezone

from .tweepy_api import get_twitter_api

API = get_twitter_api()

def set_user(user, twitter_user):
    user.user_id = twitter_user.id_str
    user.raw = twitter_user._json
    user.name = twitter_user.name
    user.username = twitter_user.screen_name
    user.description = twitter_user.description
    user.time_zone = twitter_user.time_zone or ''
    user.language = twitter_user.lang or ''
    user.url = twitter_user.url or ''
    user.verified = twitter_user.verified
    user.location = twitter_user.location
    user.account_created_on = twitter_user.created_at
    user.profile_image_url = twitter_user.profile_image_url or ''
    user.tweet_count = twitter_user.statuses_count
    user.followers_count = twitter_user.followers_count
    user.following_count = twitter_user.friends_count
    user.listed_count = twitter_user.listed_count
    user.favourites_count = twitter_user.favourites_count
    if hasattr(twitter_user, 'status'):
        user.last_status_on = twitter_user.status.created_at
    return user

def fetch_friends(user):
    from .models import User
    try:
        for tu in tweepy.Cursor(API.friends, user.username).items():
            u = User.objects.update_or_create_from_twitter(tu)
            u.followers.add(user)
    except tweepy.RateLimitError as e:
        pass

def fetch_followers(user):
    from .models import User
    try:
        for tu in tweepy.Cursor(API.followers, user.username).items():
            u = User.objects.update_or_create_from_twitter(tu)
            user.followers.add(u)
    except tweepy.RateLimitError as e:
        pass

def find_best_time_to_tweet(user):
    followers = user.followers.all()
    secs_in_day = 86400
    window = 5 # Minutes
    times = {}
    for fol in followers:
        if fol.last_status_on:
            t = fol.last_status_on.time()
            key = (t.hour, t.minute - (t.minute % window))
            times[key] = times.get(key, 0) + 1
    time_with_max_followers = max(times.iteritems(), key=operator.itemgetter(1))[0]
    return time(time_with_max_followers[0], time_with_max_followers[1], 0)
