# Generated by Django 5.0 on 2024-01-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0004_course_slug_resource_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="tgid",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]