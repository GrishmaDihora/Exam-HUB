from django.shortcuts import render_to_response
#from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('loginmodule/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loginmodule/loggedin/')
    else:
        return HttpResponseRedirect('/loginmodule/invalidlogin/')


@login_required(login_url='/loginmodule/login/')
def loggedin(request):
    c1 = {}
    c1.update(csrf(request))
    return render_to_response('loginmodule/loggedin.html', {"full_name": request.user.username}, c1)


#@login_required(login_url='/loginmodule/login/')
def invalidlogin(request):
    return render_to_response('loginmodule/invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render_to_response('loginmodule/logout.html')


def updateProfile(request):
    return render_to_response('loginmodule/updateprofile.html')


'''def transfer(request):
    c2 = {}
    c2.update(csrf(request))
    temp = request.GET.get('radio')
    request.session['name']=request.user.username
    if temp is not "Student":
        return HttpResponseRedirect('/teacher/getcourse/', c2)
'''
