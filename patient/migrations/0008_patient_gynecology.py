# Generated by Django 2.2 on 2021-04-06 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0007_auto_20210312_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Gynecology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_gyno_created_by', to=settings.AUTH_USER_MODEL)),
                ('gynecology', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Gynecology')),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_gyno_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
    ]
