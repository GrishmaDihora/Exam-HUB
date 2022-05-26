import datetime
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from teacher.models import Course, Question, Teacher
import time


def reqDisplayCourse(request):
    d = {}
    d.update(csrf(request))
    teach = Teacher.objects.all()
    d.update({'teacher': teach})
    return render_to_response('course/reqdisplay.html', d)


def displayCourse(request):
    teach_name = request.POST.get('teacher', '')
    request.session['tname'] = teach_name
    course = Course.objects.filter(teacher_name=teach_name)
    return render_to_response('course/display.html', {'course': course, 'teacher_name': teach_name})


def confirmation(request, course_id):
    # cid = request.session.get('course_id')
    request.session['course_id'] = course_id
    return render_to_response('course/confirm.html', {'course_id': course_id})


def StartExam(request):
    c = {}
    c.update(csrf(request))
    teacher_name = request.session.get('tname')
    course_id = request.session.get('course_id')
    qlist = Question.objects.filter(teacher_name=teacher_name, course_id=course_id)
    c.update({'qlist': qlist})
    new_time = qlist.count() * 240
    c.update({'new_time': new_time})
    return render_to_response('course/base.html', c)


def submitExam(request):
    a = {}
    teacher_name = request.session.get('tname')
    course_id = request.session.get('course_id')
    qlist = Question.objects.filter(teacher_name=teacher_name, course_id=course_id)
    a.update({'teacher_name': teacher_name})
    a.update({'course_id': course_id})
    score = 0
    for i in range(1, qlist.count()+1):
        user_ans = request.POST.get('op'+str(i))
        qid = request.POST.get('qid'+str(i))
        q = Question.objects.get(question_id=qid)
        if user_ans == q.answers:
            score = score + 1

    a.update({'score': score})
    a.update({'total': qlist.count()})
    return render_to_response('course/submitExam.html', a)
