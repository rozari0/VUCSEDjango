from django.urls import path

from .views import CourseView, SemesterView, index

urlpatterns = [
    path("", index, name="home"),
    path("semester/<slug:slug>/", SemesterView.as_view(), name="semester"),
    path("course/<slug:slug>/", CourseView.as_view(), name="course"),
]
