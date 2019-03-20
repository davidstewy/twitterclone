from django.db import models
from twitteruser.models import TwitterUser

class Notification(models.Model):
    notify_user = models.ForeignKey(TwitterUser, related_name='tweets', on_delete=models.CASCADE)
