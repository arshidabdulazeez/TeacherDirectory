from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='teacher_profile_pics', default='default.jpg')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25)
    room_number = models.CharField(max_length=10)
    subjects_taught = models.ManyToManyField(Subject)
