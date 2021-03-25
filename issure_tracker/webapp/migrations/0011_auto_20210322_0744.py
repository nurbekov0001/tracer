# Generated by Django 3.1.7 on 2021-03-22 07:44

from django.db import migrations, models
import webapp.validator


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20210318_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracer',
            name='surname',
            field=models.CharField(max_length=100, validators=[webapp.validator.ErrorValidator(5)], verbose_name='Краткое описание'),
        ),
    ]