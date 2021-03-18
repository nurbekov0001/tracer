# Generated by Django 3.1.7 on 2021-03-18 10:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20210317_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracer',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Разрешены символы a-zA-Z0-9', regex='^[a-zA-Z0-9]*$')], verbose_name='Полное описание'),
        ),
    ]
