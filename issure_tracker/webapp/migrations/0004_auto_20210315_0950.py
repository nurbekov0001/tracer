# Generated by Django 3.1.7 on 2021-03-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210311_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracer',
            name='type',
        ),
        migrations.AddField(
            model_name='tracer',
            name='type',
            field=models.ManyToManyField(related_name='tracers', to='webapp.Type', verbose_name='Тип'),
        ),
    ]