# Generated by Django 3.0.1 on 2020-03-14 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0045_auto_20200314_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetes',
            name='reading_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 10, 59, 12, 339389), verbose_name='تاريخ القراءة'),
        ),
    ]