from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .utils import set_user

class UserManager(models.Manager):
    def update_or_create_from_twitter(self, twitter_user):
        try:
            user = self.get(user_id=twitter_user.id_str)
        except ObjectDoesNotExist as e:
            user = self.model(user_id=twitter_user.id_str)
            user = set_user(user, twitter_user)
            user.save()
        return user

    def get_or_create_from_twitter(self, twitter_user):
        try:
            user = self.get(user_id=twitter_user.id_str)
        except ObjectDoesNotExist as e:
            user = self.model(user_id=twitter_user.id_str)
            user = set_user(user, twitter_user)
            user.save()
        return user
