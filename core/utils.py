import tweepy

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
    if twitter_user.statuses_count > 0:
        user.last_status_on = twitter_user.status.created_at
    return user

def fetch_friends(user):
    from .models import User
    for tu in tweepy.Cursor(API.friends, user.username).items():
        u = User.objects.update_or_create_from_twitter(tu)
        u.followers.add(user)
