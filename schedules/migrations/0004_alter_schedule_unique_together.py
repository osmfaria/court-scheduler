# Generated by Django 4.1.1 on 2022-09-13 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courts", "0002_initial"),
        ("schedules", "0003_alter_schedule_datetime"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="schedule",
            unique_together={("datetime", "court")},
        ),
    ]
