# Generated by Django 5.0 on 2024-01-26 12:03

import autoslug.fields
import slugify.slugify
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0007_alter_resource_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="name", slugify=slugify.slugify
            ),
        ),
    ]
