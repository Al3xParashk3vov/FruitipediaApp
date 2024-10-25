# Generated by Django 5.1.2 on 2024-10-25 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]