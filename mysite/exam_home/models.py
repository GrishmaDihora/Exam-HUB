from django.db import models


class Student(models.Model):
    s_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=200)


class Teacher(models.Model):
    t_id = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=200)
    stud_id = models.ForeignKey(Student , on_delete=models.CASCADE)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answers = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
