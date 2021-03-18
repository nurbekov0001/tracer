# Generated by Django 3.1.7 on 2021-03-17 11:18

from django.db import migrations, models
import webapp.validator


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210317_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracer',
            name='surname',
            field=models.CharField(max_length=100, validators=[webapp.validator.ErrorValidator(10)], verbose_name='Краткое описание'),
        ),
    ]
