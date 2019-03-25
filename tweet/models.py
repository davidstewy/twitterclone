from django.db import models
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    author = models.ForeignKey(TwitterUser, related_name='tweets', on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    timecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body