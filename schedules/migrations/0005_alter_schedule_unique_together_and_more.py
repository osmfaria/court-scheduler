# Generated by Django 4.1.1 on 2022-09-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0004_alter_schedule_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="schedule",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="schedule",
            constraint=models.UniqueConstraint(
                fields=("datetime", "court"), name="unique_datetime_by_court"
            ),
        ),
    ]
