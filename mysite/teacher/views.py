from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from teacher.models import Course, Question, Teacher
from loginmodule.views import *
from django.views import generic
from django.core import serializers
from django.contrib.auth.decorators import login_required


def main(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('teacher/main.html', c)


def validateTeacher(request):
    tname = request.POST.get('tname', '')
    try:
        t = Teacher.objects.get(teacher_name=tname)
        request.session['teacher_name'] = tname
        return HttpResponseRedirect('/teacher/viewcourse/'+tname+'/')
    except:
        return HttpResponseRedirect('/teacher/invalidteacher/')
    """if t is not None:
        request.session['teacher_name'] = tname
        return HttpResponseRedirect('/teacher/viewcourse/')
    else:
        return HttpResponseRedirect('/teacher/invalidteacher/')
"""


def viewCourses(request, tname):
    a = {}
    #tname = request.session.get('teacher_name')
    course = Course.objects.filter(teacher_name=tname)
    a.update({'courses': course})
    a.update({'tname': tname})
    request.session['teacher_name'] = tname
    return render_to_response('teacher/viewcourse.html', a)


def invalidTeacher(request):
    c = {}
    c.update(csrf(request))
    c.update({'wrong': 'Invalid Teacher'})
    return render_to_response('teacher/main.html', c)


def reqaddTeacher(request):
    b = {}
    b.update(csrf(request))
    return render_to_response('teacher/addTeacher.html', b)


# @login_required(login_url='/teacher/reqaddteacher/')
def addTeacher(request):
    teacher_name = request.POST.get('tname', '')
    t = Teacher(teacher_name=teacher_name)
    t.save()
    # request.session['name_teacher'] = teacher_name
    return render_to_response('teacher/teacherAdded.html')


def reqaddCourse(request, tname):
    a2 = {}
    a2.update(csrf(request))
    #tname1 = request.session.get['teacher_name']
    a2.update({'teacher': tname})
    return render_to_response('teacher/addCourse.html', a2)


# @login_required(login_url='/teacher/reqaddcourse/')
def addCourse(request):
    course_name = request.POST.get('course', '')
    course_id = request.POST.get('id', '')
    #request.session['course_id'] = course_id
    # data = serializers.serialize("json", Teacher.objects.all())
    tname = Teacher.objects.get(teacher_name=request.POST.get('tname'))
    #request.session['name_teacher'] = tname
    cour = Course(course_name=course_name, course_id=course_id, teacher_name=tname)
    cour.save()
    return render_to_response('teacher/courseadded.html')


def reqaddQuestion(request, tname, cid):
    a = {}
    a.update(csrf(request))
    #t = Teacher.objects.all()
    a.update({'teacher': tname})
    a.update({'course_id': cid})
    a.update({"tname": tname})
    return render_to_response('teacher/uploadQuestion.html', a)



# @login_required(login_url='/teacher/reqaddquestion/')
def addQuestion(request):
    q_text = request.POST.get('ques', '')
    q_id = request.POST.get('qid', '')
    c1 = request.POST.get('c1', '')
    c2 = request.POST.get('c2', '')
    c3 = request.POST.get('c3', '')
    c4 = request.POST.get('c4', '')
    ans = request.POST.get('ans', '')
    course_id = request.POST.get('cid')
    cid = Course.objects.get(course_id=course_id)
    teacher_name = request.POST.get('tane')
    tname = Teacher.objects.get(teacher_name=teacher_name)
    q = Question(teacher_name=tname, course_id=cid, question_text=q_text, answers=ans, choice_text1=c1, choice_text2=c2, choice_text3=c3, choice_text4=c4, question_id=q_id)
    q.save()
    return HttpResponseRedirect('/teacher/questionadded/'+teacher_name+'/'+course_id+'/')


# @login_required(login_url='/teacher/reqaddquestion/')
def questionAdded(request, tname, cid):
    a = {}
    a.update({'tname': tname})
    a.update({'cid': cid})
    return render_to_response('teacher/questionadded.html', a)


class CourseListView(generic.ListView):
    model = Course

# teacher_name = request.POST.get('tname', '')
# teach = Teacher.objects.filter(teacher_name)
# if teach is None:
#   t = Teacher(teacher_name=teacher_name)
#   t.save()
