# Generated by Django 3.1.2 on 2020-10-09 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentauth', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentaccount',
            old_name='phone',
            new_name='program_id',
        ),
        migrations.AddField(
            model_name='studentaccount',
            name='auth_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentauth.studentauth'),
        ),
        migrations.AddField(
            model_name='studentaccount',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='StudentAuth',
        ),
    ]