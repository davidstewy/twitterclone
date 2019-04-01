from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from twitteruser.models import TwitterUser, User
from tweet.models import Tweet
from notification.models import Notification
from twitteruser.forms import LoginForm, SignupForm


def user_view(request, author_username):
    html = 'user.html'

    TwitterUser_obj = TwitterUser.objects.filter(user__username=author_username)[0]

    Tweet_obj = Tweet.objects.filter(author=TwitterUser_obj)

    data_obj = {
        'data': {
            'user': TwitterUser_obj,
            'tweets': Tweet_obj
        }
    }

    return render(request, html, data_obj)

@login_required()
def homepage(request):
    Tweet_obj = Tweet.objects.all()

    data_obj = {
        'data': {
            'tweets': Tweet_obj,
        }
    }
    return render(request, 'homepage.html', data_obj)


def login_view(request):
    html = 'login.html'
    form = LoginForm(None or request.POST)

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
    return render(request, html, {'form': form})


def signup_view(request):
    html = "signup.html"
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'], data['password'], data['email']
            )
            login(request, user)
            TwitterUser.objects.create(
                user=user,
                username=data['username']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignupForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
