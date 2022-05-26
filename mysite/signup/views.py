from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User

# Create your views here.
from django.template.context_processors import csrf


def signup(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('signup/signup.html', c)


def addUser(request):
    uname = request.POST.get('uname')
    email = request.POST.get('email')
    password1 = request.POST.get('pass1')
    u = User.objects.create_user(password=password1, email=email, username=uname)
    u.save()
    return HttpResponseRedirect('/signup/registered/')


def registered(request):
    return render_to_response('signup/adduser.html')
