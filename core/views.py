import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import User
from .utils import fetch_friends, fetch_followers, find_best_time_to_tweet
from .tweepy_api import get_twitter_api

API = get_twitter_api()

@require_http_methods(['POST'])
def best_time_to_post(request):
    body = json.loads(request.body)
    twitter_username = body.get('username')
    force_fetch = body.get('forceFetch')
    force_fetch = False if force_fetch == 'false' else True
    twitter_user = API.get_user(twitter_username)
    user = User.objects.update_or_create_from_twitter(twitter_user)
    if force_fetch:
        fetch_friends(user)
        fetch_followers(user)
    best_time = find_best_time_to_tweet(user)
    user.best_time = best_time
    user.save()
    return JsonResponse({'username': twitter_username, 'best_time': user.best_time, 'best_day': user.best_day})
