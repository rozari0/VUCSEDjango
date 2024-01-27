# Generated by Django 5.0 on 2024-01-25 06:25

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0003_course_prereq"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default="", editable=False, populate_from="name"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resource",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=" ", editable=False, populate_from="name"
            ),
            preserve_default=False,
        ),
    ]