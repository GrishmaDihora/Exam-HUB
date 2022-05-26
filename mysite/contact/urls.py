from django.views.generic import TemplateView

from . import views
from django.urls import path

urlpatterns=[
    #path('', TemplateView.as_view(template_name='contact/contact.html', content_type='text/html')),
    path('submit/', views.submit),
    path('page/', views.contact),
    path('complete/', views.Complete),
]