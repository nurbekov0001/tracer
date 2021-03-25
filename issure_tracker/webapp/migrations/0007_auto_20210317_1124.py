# Generated by Django 3.1.7 on 2021-03-17 11:24

from django.db import migrations, models
import webapp.validator


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210317_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracer',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, validators=[webapp.validator.ErrorValidator(250)], verbose_name='Полное описание'),
        ),
    ]