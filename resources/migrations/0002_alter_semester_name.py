# Generated by Django 5.0 on 2024-01-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semester",
            name="name",
            field=models.CharField(max_length=101),
        ),
    ]
