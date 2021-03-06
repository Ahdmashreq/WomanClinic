# Generated by Django 3.0.1 on 2020-12-06 10:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import patient.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
        ('pharmacy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_Up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.CharField(blank=True, max_length=3, null=True, verbose_name='Week Number')),
                ('complain', models.CharField(blank=True, max_length=200, null=True, verbose_name='Complain')),
                ('visit_date', models.DateField(blank=True, null=True, verbose_name='Visit date')),
                ('next_visit', models.DateField(blank=True, null=True, verbose_name='Next visit date')),
                ('blood_presure', models.CharField(default='120/80', max_length=6, verbose_name='Blood presure')),
                ('protine', models.CharField(blank=True, max_length=3, null=True, verbose_name='Protine')),
                ('rbs', models.CharField(blank=True, max_length=6, null=True, verbose_name='RBS')),
                ('hemoglobin', models.CharField(blank=True, max_length=10, null=True, verbose_name='HB%')),
                ('placenta', models.CharField(blank=True, max_length=10, null=True, verbose_name='Placenta')),
                ('water', models.CharField(blank=True, max_length=6, null=True, verbose_name='Water')),
                ('fetal_position', models.CharField(blank=True, max_length=10, null=True, verbose_name='Fetal position')),
                ('fetal_movement', models.CharField(blank=True, max_length=10, null=True, verbose_name='Fetal movement')),
                ('fetal_heart_rate', models.CharField(blank=True, max_length=10, null=True, verbose_name='Fetal heart rate')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight')),
                ('exit_nature', models.CharField(blank=True, choices=[('better', 'Better'), ('responsibility', 'Responsibility'), ('scape', 'Scape')], max_length=50, null=True, verbose_name='Exit Nature')),
                ('exit_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Responsibility')),
                ('surgery', models.CharField(blank=True, choices=[('curettage_cleaning', 'Dilatation & Curettage'), ('cervical_stitch', 'Cervical Cerclage'), ('ectopic_pregnancy', 'Ectopic Pregnancy'), ('CS', 'Cesarean Delivery')], max_length=50, null=True, verbose_name='Surgery')),
                ('surgery_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Surgery desc')),
                ('clexane_sarf_date', models.DateField(blank=True, null=True, verbose_name='Clexane issue date')),
                ('mhx', models.TextField(blank=True, max_length=255, null=True, verbose_name='MHx')),
                ('shx', models.TextField(blank=True, max_length=255, null=True, verbose_name='SHx')),
                ('allergy_hx', models.TextField(blank=True, max_length=255, null=True, verbose_name='Allergy Hx')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_up_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_up_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Patient Name')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('job', models.CharField(max_length=30, verbose_name='Job')),
                ('husband_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Husband Name')),
                ('husband_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Husband Phone')),
                ('g', models.PositiveIntegerField(blank=True, null=True, verbose_name='G')),
                ('p', models.PositiveIntegerField(blank=True, null=True, verbose_name='P')),
                ('pre', models.PositiveIntegerField(blank=True, null=True, verbose_name='PRE')),
                ('insurance_number', models.PositiveIntegerField(verbose_name='Insurance Number')),
                ('entrance_number', models.PositiveIntegerField(verbose_name='Enterance Number')),
                ('hospital_number', models.PositiveIntegerField(verbose_name='Hospital Number')),
                ('patient_number', models.PositiveIntegerField(verbose_name='Patient Number')),
                ('room', models.CharField(max_length=70, verbose_name='Room')),
                ('hospital_section', models.CharField(blank=True, max_length=70, null=True, verbose_name='Section')),
                ('transferred_from', models.CharField(blank=True, choices=[('insurance', 'Medical Insurance'), ('consultant', 'Consultant Doctor'), ('outpatient', 'Outside Doctor'), ('patient', 'Patient himself')], max_length=70, null=True, verbose_name='Patient Transferred From')),
                ('clexane_order_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Clexane Order Number')),
                ('entrance_date', models.DateField(blank=True, null=True, verbose_name='Enterance Date')),
                ('patient_type', models.CharField(blank=True, choices=[('CHECK_UP', 'Check up'), ('CONSULTANT', 'Consultant'), ('OPERATION', 'GYN operations'), ('DELIVER', 'Delivery')], max_length=50, null=True, verbose_name='Patient Type')),
                ('exit_date', models.DateField(blank=True, null=True, verbose_name='Exit Date')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_created_by', to=settings.AUTH_USER_MODEL)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic', verbose_name='Hospital')),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ultrasound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prognosis', models.TextField(max_length=250, verbose_name='Prognosis')),
                ('visit_date', models.DateField(default=datetime.date.today, verbose_name='Visit date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('check_up', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Check_Up', verbose_name='Follow up')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ultrasound_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ultrasound_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=datetime.date.today, verbose_name='Issue date')),
                ('dose', models.PositiveIntegerField(verbose_name='Dose')),
                ('notes', models.CharField(blank=True, max_length=250, null=True, verbose_name='Notes')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('check_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Check_Up', verbose_name='Follow up')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_med_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_med_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Medicine', verbose_name='Medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_name', models.CharField(max_length=150, verbose_name='File Name')),
                ('attachment', models.FileField(blank=True, null=True, upload_to=patient.models.path_and_rename, verbose_name='Attachment')),
                ('start_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_attach_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_attach_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Exit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exit_date', models.DateField(blank=True, null=True, verbose_name='Exit Date')),
                ('exit_diagnosis', models.CharField(blank=True, max_length=70, null=True, verbose_name='Exit Diagnosis')),
                ('exit_nature', models.CharField(blank=True, choices=[('better', 'Better'), ('responsibility', 'Responsibility'), ('scape', 'Scape')], max_length=50, null=True, verbose_name='Exit Nature')),
                ('physician', models.CharField(blank=True, max_length=150, null=True, verbose_name='Physician')),
                ('resident_doctor', models.CharField(blank=True, max_length=150, null=True, verbose_name='Resident Doctor')),
                ('date_start', models.DateField(verbose_name='Days-off Start Date')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Days-off End Date')),
                ('exit_note', models.TextField(blank=True, max_length=250, null=True, verbose_name='Exit Note')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Days_Off',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='Days-off Start Date')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Days-off End Date')),
                ('num_of_days', models.PositiveIntegerField(verbose_name='Number of days')),
                ('notes', models.CharField(blank=True, max_length=250, null=True, verbose_name='Notes')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_day_off_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_day_off_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_day_off', to='patient.Patient', verbose_name='Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Past_Medical_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes', models.BooleanField(blank=True, null=True, verbose_name='Diabetes')),
                ('pulmonar', models.BooleanField(blank=True, null=True, verbose_name='Pulmonar')),
                ('hypertension', models.BooleanField(blank=True, null=True, verbose_name='Hypertension')),
                ('allergies', models.BooleanField(blank=True, null=True, verbose_name='Allergies')),
                ('heart_disease', models.BooleanField(blank=True, null=True, verbose_name='Heart Disease')),
                ('breast', models.BooleanField(blank=True, null=True, verbose_name='Breast')),
                ('autoimmun_disorder', models.BooleanField(blank=True, null=True, verbose_name='Autoimmun Disorder')),
                ('autoimmun_disorder_value', models.CharField(blank=True, max_length=50, null=True, verbose_name='Autoimmun Disorder Value')),
                ('abnormal_pap', models.CharField(blank=True, max_length=50, null=True, verbose_name='Abnormal PAP')),
                ('kidney_disease', models.BooleanField(blank=True, null=True, verbose_name='Kidney Disease')),
                ('kidney_disease_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kidney Disease Value')),
                ('uterine', models.CharField(blank=True, max_length=50, null=True, verbose_name='Uterine')),
                ('psychiatric', models.BooleanField(blank=True, null=True, verbose_name='PSYCHIATRIC')),
                ('infertility', models.CharField(blank=True, max_length=255, null=True, verbose_name='INFERTILITY')),
                ('neurologic', models.BooleanField(blank=True, null=True, verbose_name='NEUROLOGIC')),
                ('rfh', models.CharField(blank=True, max_length=50, null=True, verbose_name='RFH')),
                ('hld', models.BooleanField(blank=True, null=True, verbose_name='HLD')),
                ('hld_value', models.CharField(blank=True, max_length=20, null=True, verbose_name='HLD Value')),
                ('gyns', models.CharField(blank=True, max_length=255, null=True, verbose_name='GYNS')),
                ('varicosities', models.BooleanField(blank=True, null=True, verbose_name='VARICOSITIES')),
                ('operation', models.CharField(blank=True, max_length=255, null=True, verbose_name='OPERATION')),
                ('thyroid_dysfunction', models.BooleanField(blank=True, null=True, verbose_name='THYROID DYSFUNCTION')),
                ('thyroid_dysfunction_value', models.CharField(blank=True, choices=[('hypo', 'HYPO'), ('hyper', 'HYPER')], max_length=20, null=True, verbose_name='THYROID DYSFUNCTION Value')),
                ('anesthetic', models.CharField(blank=True, choices=[('GA', 'GA'), ('SA', 'SA')], max_length=20, null=True, verbose_name='ANESTHETIC')),
                ('trauma', models.CharField(blank=True, max_length=255, null=True, verbose_name='Trauma')),
                ('history_of_blood_transfusion', models.BooleanField(blank=True, null=True, verbose_name='History Of Blood Transfusion')),
                ('history_of_blood_transfusion_value', models.CharField(blank=True, max_length=20, null=True, verbose_name='History Of Blood Transfusion Value')),
                ('othr', models.CharField(blank=True, max_length=255, null=True, verbose_name='other')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_history_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_history_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Gynecology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_en', models.CharField(max_length=200, verbose_name='Diagnosis EN')),
                ('diagnosis_ar', models.CharField(max_length=200, verbose_name='Diagnosis AR')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gyno_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gyno_last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bs', models.PositiveIntegerField(verbose_name='Blood sugar')),
                ('bp_up', models.PositiveIntegerField(default=120, verbose_name='BP Up')),
                ('bp_down', models.PositiveIntegerField(default=80, verbose_name='BP Down')),
                ('temp', models.PositiveIntegerField(default=37, verbose_name='Temprature')),
                ('reading_date', models.DateTimeField(default=datetime.datetime(2020, 12, 6, 12, 11, 41, 478664), verbose_name='reading date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diabetes_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diabetes_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_diabetes', to='patient.Patient', verbose_name='Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Delivery Notes')),
                ('type', models.CharField(blank=True, choices=[('n', 'NVD'), ('c', 'LSCS')], max_length=30, null=True, verbose_name='Delivery Types')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Delivery Hospital')),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Delivery Date')),
                ('anesthesia_type', models.CharField(blank=True, choices=[('S', 'Spinal anesthesia'), ('G', 'General anesthesia')], max_length=50, null=True, verbose_name='Anesthesia Type')),
                ('anesthesia_doc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anesthesia Doctor')),
                ('abo_rh', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=50, null=True, verbose_name='Blood Type')),
                ('fetal_sex', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('t', 'Twins')], max_length=50, null=True, verbose_name='Fetal Sex')),
                ('lnmp', models.DateField(blank=True, null=True, verbose_name='Last Period Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient', verbose_name='Patient')),
            ],
        ),
        migrations.AddField(
            model_name='check_up',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient', verbose_name='Patient'),
        ),
    ]
