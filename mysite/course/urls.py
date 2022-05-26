from django.urls import path
from . import views

urlpatterns = [
    path('confirmation/<str:course_id>/', views.confirmation),
    path('startexam/', views.StartExam),
    path('reqdisplay/', views.reqDisplayCourse),
    path('display/', views.displayCourse),
    path('submitexam/', views.submitExam),
   # path('selectcourse/', views.selectCourse),

]
