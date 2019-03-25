from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet

def homepage(request):
    return render(request, 'homepage.html')
