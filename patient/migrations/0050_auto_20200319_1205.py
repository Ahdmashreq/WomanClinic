# Generated by Django 3.0.1 on 2020-03-19 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0049_auto_20200319_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='past_medical_history',
            name='othrt',
        ),
        migrations.AddField(
            model_name='past_medical_history',
            name='othr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='othr'),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='reading_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 12, 5, 35, 722758), verbose_name='تاريخ القراءة'),
        ),
    ]