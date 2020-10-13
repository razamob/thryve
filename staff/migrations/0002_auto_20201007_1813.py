# Generated by Django 3.1.2 on 2020-10-07 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffauth',
            name='staff_id',
        ),
        migrations.AddField(
            model_name='staffaccount',
            name='auth_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staffauth'),
        ),
    ]