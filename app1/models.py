from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    time = models.TimeField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
