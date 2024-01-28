from django.shortcuts import render
from django.views.generic import DetailView

from resources.models import Course, Semester


# Create your views here.
def index(request):
    semester = Semester.objects.all()
    return render(
        request, template_name="resources/index.html", context={"semesters": semester}
    )


class SemesterView(DetailView):
    model = Semester
    template_name = "resources/semester.html"
    context_object_name = "semesters"


class CourseView(DetailView):
    model = Course
    template_name = "resources/course.html"
    context_object_name = "courses"
