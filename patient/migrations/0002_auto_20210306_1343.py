# Generated by Django 2.2 on 2021-03-06 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='past_medical_history',
            name='allergies_list',
            field=models.CharField(blank=True, choices=[('food', 'طعام'), ('med', 'ادوية'), ('chemical', 'مواد كيميائية'), ('chest', 'حساسية صدر'), ('nose', 'جيوب أنفية')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='past_medical_history',
            name='allergies_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Allergies Name'),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='reading_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='reading date'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='allergies',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Allergies'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='autoimmun_disorder',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Autoimmun Disorder'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='autoimmun_disorder_value',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Autoimmun Disorder Name'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='breast',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Breast'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='diabetes',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='heart_disease',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Heart Disease'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='history_of_blood_transfusion',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='History Of Blood Transfusion'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='history_of_blood_transfusion_value',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='History Of Blood Transfusion Name'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='hld',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='HLD'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='hld_value',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='HLD Name'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='hypertension',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Hypertension'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='kidney_disease',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Kidney Disease'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='kidney_disease_value',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kidney Disease Name'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='neurologic',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='NEUROLOGIC'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='psychiatric',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='PSYCHIATRIC'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='pulmonar',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Pulmonar'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='thyroid_dysfunction',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='THYROID DYSFUNCTION'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='thyroid_dysfunction_value',
            field=models.CharField(blank=True, choices=[('hypo', 'HYPO'), ('hyper', 'HYPER')], max_length=20, null=True, verbose_name='THYROID DYSFUNCTION Name'),
        ),
        migrations.AlterField(
            model_name='past_medical_history',
            name='varicosities',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='VARICOSITIES'),
        ),
    ]
