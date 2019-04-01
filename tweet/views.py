from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from tweet.forms import TweetForm

def tweet_by_id(request, author_username, tweet_id):
    html = "tweet.html"

    TwitterUser_obj = TwitterUser.objects.filter(user__username=author_username)[0]

    Tweet_obj = Tweet.objects.all().filter(author=TwitterUser_obj).filter(id=tweet_id)

    data_obj = {
        'data': {
            'user': TwitterUser_obj,
            'tweets':Tweet_obj
        }
    }
    return render(request, html, data_obj)


@login_required()
def new_tweet(request):
    html = 'new_tweet.html'
    form = TweetForm()
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(author=request.user.author, body=data['body'])

        return HttpResponseRedirect('/')
    return render(request, html, {'form':form})
