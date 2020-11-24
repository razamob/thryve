# Generated by Django 3.1.2 on 2020-10-24 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sso', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sso', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='CareerCounselorForm',
        ),
        migrations.DeleteModel(
            name='EmploymentConsultantForm',
        ),
    ]