from django.urls import path
from tweet.views import tweet_by_id, new_tweet

urlpatterns = [
    path('<str:author_username>/<int:tweet_id>/', tweet_by_id),
    path('tweet/', new_tweet)
]