from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("schedule_interview/", views.schedule_interview, name="schedule_interview"),
    path("interviews/", views.interviews, name="interviews"),
    path("edit/", views.edit, name="edit"),
    path("create_slot", views.create_slot, name="create_slot"),
]
