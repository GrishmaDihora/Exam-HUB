from django.db import models

class Teacher(models.Model):
    # teacher_id = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=200, primary_key=True)
    # stud_id = models.ForeignKey(Student , on_delete=models.CASCADE)


class Course(models.Model):
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=100, primary_key=True)
    course_name = models.CharField(max_length=150)

    def __str__(self):
        return self.course_name


class Question(models.Model):
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_id = models.CharField(max_length=50, primary_key=True)
    question_text = models.CharField(max_length=400)
    answers = models.CharField(max_length=200)
    choice_text1 = models.CharField(max_length=200)
    choice_text2 = models.CharField(max_length=200)
    choice_text3 = models.CharField(max_length=200)
    choice_text4 = models.CharField(max_length=200)
