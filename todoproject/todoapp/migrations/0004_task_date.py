# Generated by Django 3.2.16 on 2022-10-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-03-11'),
            preserve_default=False,
        ),
    ]
