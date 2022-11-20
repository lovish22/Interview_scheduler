from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Student, Interviewer, Interview
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from interview_scheduler.settings import BASE_DIR
import os, sys


def homepage(request):
    return render(request, "app/homepage.html")


def time_float(res):
    hr = int(res[:2])
    min = int(res[3:])
    min = min / 60
    hr += min
    return hr


def schedule_interview(request):
    students = Student.objects.all()
    interviewers = Interviewer.objects.all()
    context = {"students": students, "interviewers": interviewers}
    return render(request, "app/schedule_interview.html", context)


def interviews(request):
    interviews = Interview.objects.all()
    context = {"interviews": interviews}
    return render(request, "app/interviews.html", context)


def create_slot(request):
    student = request.POST["student"]
    interviewer = request.POST["interviewer"]
    start_time = request.POST["start_time"]
    end_time = request.POST["end_time"]

    st_time = time_float(start_time)
    ed_time = time_float(end_time)

    arr1 = Interview.objects.get(student=student)
    arr2 = Interview.objects.get(interviewer=interviewer)

    for i in arr1:
        res = i.start_time.hour
        res += ":"
        res += i.start_time.min
        beg_time = time_float(res)

        res = i.end_time.hour
        res += ":"
        res += i.end_time.min
        fin_time = time_float(res)

        if st_time > fin_time or ed_time < beg_time:
            continue
        else:
            return HttpResponseRedirect(reverse("schedule_interview"))

    for i in arr2:
        res = i.start_time.hour
        res += ":"
        res += i.start_time.min
        beg_time = time_float(res)

        res = i.end_time.hour
        res += ":"
        res += i.end_time.min
        fin_time = time_float(res)

        if st_time > fin_time or ed_time < beg_time:
            continue
        else:
            return HttpResponseRedirect(reverse("schedule_interview"))

    recent_creation = Interview()
    recent_creation.student = student
    recent_creation.interviewer = interviewer
    recent_creation.start_time = start_time
    recent_creation.end_time = end_time

    recent_creation.save()
    return HttpResponseRedirect(reverse("interviews"))


def edit(request):
    return render(request, "app/edit.html")
