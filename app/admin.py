from django.contrib import admin

from .models import Student, Interviewer, Interview

admin.site.register(Student)
admin.site.register(Interviewer)
admin.site.register(Interview)
