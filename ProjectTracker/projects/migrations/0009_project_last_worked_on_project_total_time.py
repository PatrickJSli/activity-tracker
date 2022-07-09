# Generated by Django 4.0.5 on 2022-07-09 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_rename_derscription_milestone_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_worked_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 18, 25, 58, 480383)),
        ),
        migrations.AddField(
            model_name='project',
            name='total_time',
            field=models.IntegerField(default=0),
        ),
    ]
