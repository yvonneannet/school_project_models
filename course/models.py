from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    credits = models.IntegerField()
    department = models.CharField(max_length=50)
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)
    syllabus = models.TextField()
    course_duration = models.IntegerField()  # in weeks
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.course_name