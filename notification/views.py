from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from notification.models import Notification

def homepage(request):
    pageoptions = {}
    newdictionary = {'test': 'testing notification'}
    pageoptions.update(newdictionary)
    return render(request, 'homepage.html', pageoptions)