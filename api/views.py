from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CourseSerializer, ResourceSerializer, SemesterSerializer
from resources.models import Course, Resource, Semester

# Create your views here.


class SemesterApiView(APIView):
    def get(self, request, *args, **kwargs):
        semesters = Semester.objects.all()
        serializer = SemesterSerializer(semesters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SemesterDetailApiView(APIView):
    def get_object(self, semester_id):
        try:
            return Semester.objects.get(id=semester_id)
        except Semester.DoesNotExist:
            return None

    def get(self, request, semester_id, *args, **kwargs):
        semester = self.get_object(semester_id)
        if not semester:
            return Response(
                {"res": "Object with semester id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = SemesterSerializer(semester)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseDetailApiView(APIView):
    def get_object(self, course_id):
        try:
            return Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return None

    def get(self, request, course_id, *args, **kwargs):
        course = self.get_object(course_id)
        if not course:
            return Response(
                {"res": "Object with semester id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ResourceDetailApiView(APIView):
    def get_object(self, resource_id):
        try:
            return Resource.objects.get(id=resource_id)
        except Resource.DoesNotExist:
            return None

    def get(self, request, resource_id, *args, **kwargs):
        resource = self.get_object(resource_id)
        if not resource:
            return Response(
                {"res": "Object with resource id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ResourceSerializer(resource)
        return Response(serializer.data, status=status.HTTP_200_OK)
