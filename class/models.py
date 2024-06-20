from django.db import models

from .models import Teacher 

from .models import Student

from .models import Course


# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=10)
    schedule = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name} - {self.section}"
