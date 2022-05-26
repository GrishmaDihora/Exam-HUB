from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic


def mainRedirect(request):
    return HttpResponseRedirect('/home/')


