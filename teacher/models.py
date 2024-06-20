from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    hire_date = models.DateField()
    department = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    salary = models.FloatField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
