from django.urls import path
from django.shortcuts import render
from .views import (
    CourseDetailApiView,
    ResourceDetailApiView,
    SemesterApiView,
    SemesterDetailApiView,
)

urlpatterns = [
    path("semesters/", SemesterApiView.as_view(), name="apisemesters"),
    path(
        "semester/<int:semester_id>/",
        SemesterDetailApiView.as_view(),
        name="apisemester",
    ),
    path("course/<int:course_id>/", CourseDetailApiView.as_view(), name="apicourse"),
    path(
        "resource/<int:resource_id>/",
        ResourceDetailApiView.as_view(),
        name="apiresource",
    ),
    path("", lambda request: render(request, "api/index.html")),
]
