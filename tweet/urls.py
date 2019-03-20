from django.urls import path
from tweet.views import homepage

urlpatterns = [
    path('tweet', homepage, name='tweet'),
]