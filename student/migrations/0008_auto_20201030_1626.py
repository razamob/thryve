# Generated by Django 3.1.2 on 2020-10-30 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentauth', '0001_initial'),
        ('student', '0007_auto_20201030_1409'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentaccount',
            unique_together={('fname', 'lname', 'email', 'student_number', 'phone_number', 'program_year', 'als', 'coop', 'international', 'auth_id')},
        ),
    ]
