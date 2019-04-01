from django.urls import path
from twitteruser.views import homepage, login_view, signup_view, logout_view, user_view

urlpatterns = [
    path('', homepage, name='homepage'),  
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('<str:author_username>/', user_view, name='profile')
]