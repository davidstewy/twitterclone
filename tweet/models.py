from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    timecreated = models.DateTimeField(auto_now_add=True)
