# Generated by Django 3.0.4 on 2020-11-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20201111_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaccount',
            name='grade',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
