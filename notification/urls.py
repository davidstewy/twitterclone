from django.urls import path
from notification.views import homepage

urlpatterns = [
    path('notification', homepage, name='notification'),
]