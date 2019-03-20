from django.urls import path
from twitteruser.views import homepage

urlpatterns = [
    path('twitteruser', homepage, name='twitteruser'),
]