from django.urls import path
from django.views.generic import TemplateView
from . import views
from loginmodule.views import login, auth_view, logout, loggedin, invalidlogin
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('main/', views.main),
    path('validate/', views.validateTeacher),
    path('viewcourse/<str:tname>/', views.viewCourses),
    path('invalidteacher/', views.invalidTeacher),
    path('reqaddteacher/', views.reqaddTeacher),
    path('addteacher/', views.addTeacher),

    path('reqaddcourse/<str:tname>/', views.reqaddCourse),
    path('addcourse/', views.addCourse),

    path('addquestion/', views.addQuestion),
    path('questionadded/<str:tname>/<int:cid>/', views.questionAdded),
    path('reqaddquestion/<str:tname>/<int:cid>/', views.reqaddQuestion),
    path('courses/', views.CourseListView.as_view(), name='course')

]
