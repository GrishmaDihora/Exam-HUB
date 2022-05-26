from django.urls import path
from django.views.generic import TemplateView

from loginmodule.views import login, auth_view, logout, loggedin, invalidlogin, updateProfile
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout),
    url(r'^loggedin/$', loggedin),
    url(r'^invalidlogin/$', invalidlogin),
    path('updateprofile/', updateProfile),
    #url(r'^signup/$', TemplateView.as_view(template_name='loginmodule/signup.html',content_type='text/html')),
    #path('transfer/', transfer),
]