from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('home/', TemplateView.as_view(template_name='exam_home/index.html', content_type='text/html')),
    path('', views.mainRedirect),

]