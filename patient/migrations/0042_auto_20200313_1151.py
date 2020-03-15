# Generated by Django 3.0.1 on 2020-03-13 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0041_auto_20200313_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='notes',
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='reading_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 13, 11, 51, 56, 710509), verbose_name='تاريخ القراءة'),
        ),
        migrations.AlterField(
            model_name='patient_exit',
            name='exit_note',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='ملاحظات الخروج'),
        ),
    ]