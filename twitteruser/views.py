from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from twitteruser.models import TwitterUser, User
from tweet.models import Tweet
from notification.models import Notification
from twitteruser.forms import LoginForm, SignupForm


def homepage(request):
    return render(request, 'homepage.html')


def login_view(request):
    html = 'login.html'
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
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
