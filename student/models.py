from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
       ('M','Male'),
       ('F','Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, default='Female')
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=3, null=False, default='Code')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

def __str__(self):
 return f"{self.first_name} {self.last_name}"




