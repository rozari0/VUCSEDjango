from django.contrib import admin

from .models import Course, Resource, Semester, TgResource

# Register your models here.


class TgResourceInline(admin.StackedInline):
    model = TgResource


class ResourceAdmin(admin.ModelAdmin):
    inlines = [TgResourceInline]


admin.site.register(Resource, ResourceAdmin)

admin.site.register(Course)

admin.site.register(Semester)
