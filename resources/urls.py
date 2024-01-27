from django.urls import path

from .views import (
    CourseDetailApiView,
    CourseView,
    ResourceDetailApiView,
    SemesterApiView,
    SemesterDetailApiView,
    SemesterView,
    index,
)

urlpatterns = [
    path("", index, name="home"),
    path("semester/<slug:slug>/", SemesterView.as_view(), name="semester"),
    path("course/<slug:slug>/", CourseView.as_view(), name="course"),
    path("api/semesters/", SemesterApiView.as_view()),
    path("api/semester/<int:semester_id>/", SemesterDetailApiView.as_view()),
    path("api/course/<int:course_id>/", CourseDetailApiView.as_view()),
    path("api/resource/<int:resource_id>/", ResourceDetailApiView.as_view()),
]
