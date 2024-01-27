from rest_framework import serializers

from .models import Course, Resource, Semester


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        depth = 1
        fields = ["id", "name", "slug", "course"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        depth = 1
        fields = ["id", "name", "resource", "semester"]


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        depth = 1
        fields = ["id", "name", "description", "link", "tg", "course"]
