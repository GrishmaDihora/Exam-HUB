from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from firstdbtest.models import Student


def getstudentinfo(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('firstdbtest/addstudentinfo.html', c)


def addstudentinfo(request):
    sname = request.POST.get('studentname', '')
    sdate = request.POST.get('birthdate', '')
    s = Student(student_name = sname, student_dob=sdate)
    s.save()
    return HttpResponseRedirect('/firstdbtest/addsuccess/')


def addsuccess(request):
    return render_to_response('firstdbtest/addrecord.html')


class StudentListView(generic.ListView):
    model = Student

