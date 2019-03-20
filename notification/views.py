from django.shortcuts import render, HttpResponseRedirect, reverse

def homepage(request):
    pageoptions = {}
    newdictionary = {'test': 'testing notification'}
    pageoptions.update(newdictionary)
    return render(request, 'homepage.html', pageoptions)