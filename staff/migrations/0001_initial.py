# Generated by Django 3.0.4 on 2020-10-27 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=30, null=True)),
                ('job_code', models.IntegerField()),
                ('job_title', models.CharField(max_length=50)),
                ('auth_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.StaffAuth')),
            ],
        ),
    ]
