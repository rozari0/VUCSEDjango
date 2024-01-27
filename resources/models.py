from autoslug import AutoSlugField
from django.db import models
from slugify import slugify


class Semester(models.Model):
    name = models.CharField(max_length=101)
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    semester = models.ForeignKey(Semester, models.CASCADE, related_name="course")
    code = models.CharField(max_length=50)
    prereq = models.ForeignKey("self", models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(populate_from="name", slugify=slugify)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, models.CASCADE, related_name="resource")
    description = models.TextField()
    slug = AutoSlugField(populate_from="name")
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class TgResource(models.Model):
    name = models.CharField(max_length=100)
    m_id = models.PositiveBigIntegerField()
    mainresource = models.ForeignKey(Resource, models.CASCADE, related_name="tg")
