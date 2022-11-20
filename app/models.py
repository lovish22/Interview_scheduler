from django.db import models
from asyncio.windows_events import NULL
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Interviewer(models.Model):
    name = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Interview(models.Model):
    interview_id = models.CharField(max_length=200, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
