import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import User
from .utils import fetch_friends
from .tweepy_api import get_twitter_api

API = get_twitter_api()

@require_http_methods(['POST'])
def best_time_to_post(request):
    twitter_username = json.loads(request.body).get('username')
    twitter_user = API.get_user(twitter_username)
    user = User.objects.update_or_create_from_twitter(twitter_user)
    fetch_friends(user)
    return JsonResponse({'username': twitter_username, 'best_time': user.best_time, 'best_day': user.best_day})
