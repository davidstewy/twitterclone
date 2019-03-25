from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    username = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return self.username