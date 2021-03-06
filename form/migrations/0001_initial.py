# Generated by Django 3.0.6 on 2020-06-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerCounselorForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1_sso', models.BooleanField(default=False)),
                ('q1_friend', models.BooleanField(default=False)),
                ('q1_faculty', models.BooleanField(default=False)),
                ('q1_visit', models.BooleanField(default=False)),
                ('q1_orient', models.BooleanField(default=False)),
                ('q1_event', models.BooleanField(default=False)),
                ('q1_kpi', models.BooleanField(default=False)),
                ('q1_outreach', models.BooleanField(default=False)),
                ('q1_posters', models.BooleanField(default=False)),
                ('q1_stv', models.BooleanField(default=False)),
                ('q1_social', models.BooleanField(default=False)),
                ('q1_media', models.BooleanField(default=False)),
                ('ccs_resume', models.BooleanField(default=False)),
                ('ccs_cover', models.BooleanField(default=False)),
                ('ccs_interview', models.BooleanField(default=False)),
                ('ccs_jobsearch', models.BooleanField(default=False)),
                ('ccs_mockinterview', models.BooleanField(default=False)),
                ('ccs_networking', models.BooleanField(default=False)),
                ('ccs_portfolio', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentConsultantForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1_sso', models.BooleanField(default=False)),
                ('q1_friend', models.BooleanField(default=False)),
                ('q1_faculty', models.BooleanField(default=False)),
                ('q1_visit', models.BooleanField(default=False)),
                ('q1_orient', models.BooleanField(default=False)),
                ('q1_event', models.BooleanField(default=False)),
                ('q1_kpi', models.BooleanField(default=False)),
                ('q1_outreach', models.BooleanField(default=False)),
                ('q1_posters', models.BooleanField(default=False)),
                ('q1_stv', models.BooleanField(default=False)),
                ('q1_social', models.BooleanField(default=False)),
                ('q1_media', models.BooleanField(default=False)),
                ('ccs_resume', models.BooleanField(default=False)),
                ('ccs_cover', models.BooleanField(default=False)),
                ('ecs_exploration', models.BooleanField(default=False)),
                ('ecs_eplanning', models.BooleanField(default=False)),
                ('ecs_cplanning', models.BooleanField(default=False)),
                ('ecs_labourmarket', models.BooleanField(default=False)),
                ('ecs_other', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
