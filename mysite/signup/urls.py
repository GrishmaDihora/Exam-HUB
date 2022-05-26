from django.urls import path
from django.conf import urls

from . import views

urlpatterns = [
    path('', views.signup),
    path('registered/', views.registered),
    path('adduser/', views.addUser),

]
