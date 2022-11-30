from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    roll = models.IntegerField()

    def __str__(self):
        return self.name
